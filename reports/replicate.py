'''Replicate data from Firebird database (isiac) to Postgres'''
import logging
import datetime
import fdb
import psycopg2


logging.basicConfig(
    filename="replicate.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s")

YEAR_NOW = 2019

def get_ticket_id(con, cursor, ticket_num):
    ''' Return ticket ID if found'''
    try:
        cursor.execute("""
            SELECT id FROM reports_tickets WHERE ticket = '%s' AND year=%s;
            """, (ticket_num, YEAR_NOW))
    except Exception as exp:
        logging.debug(exp)

    con.commit()
    return cursor.fetchone()

def get_device_id(con, cursor, row):
    ''' Return device ID'''
    try:
        cursor.execute("""
            SELECT id FROM reports_device WHERE invent_number = %s AND serial_number = %s;
            """, (row['invnumber'], row['sernumber']))
    except Exception as exp:
        logging.debug(exp)
    con.commit()
    device_id = cursor.fetchone()

    if not device_id:
        try:
            cursor.execute("""
                INSERT INTO reports_device (invent_number, serial_number, name)
                    VALUES (%s,%s,%s) RETURNING id;
                """, (row['invnumber'], row['sernumber'], row['stationname'][:80]))
        except Exception as exp:
            logging.debug(exp)
        con.commit()
        device_id = cursor.fetchone()
        logging.info("Inserted device %s I/N %s", row['stationname'], row['invnumber'])

    return device_id

def insert_ticket(con, cursor, row, device_id):
    ''' Add new row to Tickets'''
    select = """
            INSERT INTO reports_tickets 
                (ticket, remark, court_id, device_id, year, co7_date,died)
              VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id;
            """
    try:
        cursor.execute(select, (row['regnum'], row['problemdscrptn'],\
                  row['vn_code'], device_id, YEAR_NOW, row['regdate'].date(), False))
    except Exception as exp:
        logging.debug(exp)

    logging.info("Inserted ticket №%s", row['regnum'])
    con.commit()

def update_ticket(con, cursor, ticket_close_date, ticket_id):
    ''' Set ticket close date if not null'''
    try:
        cursor.execute("""
            UPDATE reports_tickets SET co8_date = %s WHERE id = %s 
            """, (ticket_close_date, ticket_id))
    except Exception as exp:
        logging.debug(exp)
    con.commit()
    logging.info("Update ticket ID %s date %s", ticket_id, ticket_close_date)

def main():
    ''' Main function'''
    try:
        con = fdb.connect(dsn='192.168.10.10:cia', user='SYSDBA', password='m')
        cursorfb = con.cursor()
    except Exception as exp:
        logging.debug(exp)
        return

    cursorfb = con.cursor()
    select = "SELECT  sr.INVNUMBER, sr.SERNUMBER, sr.REGNUM, sr.REGYEAR,\
		            sr.REZULTID, sr.EXECUTEDT, SERVICEREQUESTEQPMNTCHECK.problemdscrptn,\
		            TERMINALEQUIPMENT.stationname, INSTITUTION.vn_code, sr.REGDATE\
		    FROM servicerequest AS sr\
		    JOIN SERVICEREQUESTEQPMNTCHECK ON sr.id = SERVICEREQUESTEQPMNTCHECK.requestid\
		    JOIN TERMINALEQUIPMENT         ON sr.equipmentid   = TERMINALEQUIPMENT.id\
		    JOIN INSTITUTION               ON sr.INSTITUTIONID = INSTITUTION.id\
		    WHERE sr.REGYEAR = 2019 and\
                SERVICEREQUESTEQPMNTCHECK.problemdscrptn is not null and\
                sr.INVNUMBER is not null;"
    cursorfb.execute(select)
    rowmap = cursorfb.fetchallmap()
    con.commit()
    cursorfb.close()
    con.close()

    try:
        con = psycopg2.connect("dbname='repairs' user='postgres' \
                                host='192.168.10.20' password='postgres'")
    except Exception as exp:
        logging.debug(exp)
        return
    cursor = con.cursor()

    for row in rowmap: 
        ticket_id = get_ticket_id(con, cursor, row['regnum'])
        if not ticket_id:
            # Insert ticket but check device exists before
            device_id = get_device_id(con, cursor, row)
            insert_ticket(con, cursor, row, device_id)

        if row['executedt']:
            # If ticket close date (executedt) is not null update it
            update_ticket(con, cursor, row['executedt'], ticket_id)

    cursor.close()
    con.commit()
    con.close()
