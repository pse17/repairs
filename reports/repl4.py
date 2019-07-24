import fdb
import psycopg2
YEAR_NOW = 2019

def get_tickets(pgcon, pgcursor):
    select = "SELECT ticket FROM reports_ticket"
    pgcursor.execute(select)
    tickets = pgcursor.fetchall()
    pgcon.commit()
    return tickets

def feel_temp_table(fbcon, fbcursor, tickets):
    temp_table_create = "CREATE GLOBAL TEMPORARY table TEMP_TICKETS (REGNUM integer) ON COMMIT PRESERVE ROWS"
    fbcursor.execute(temp_table_create)
    fbcon.commit()

    for ticket in tickets:
        insert = "INSERT INTO TEMP_TICKETS VALUES (%s)" % ticket
        fbcursor.execute(insert)
    fbcon.commit()


def get_new_tickets(fbcon, fbcursor):
    select = "SELECT  sr.INVNUMBER, sr.SERNUMBER, sr.REGNUM, sr.REGYEAR,\
		            sr.REZULTID, sr.EXECUTEDT, SERVICEREQUESTEQPMNTCHECK.problemdscrptn,\
		            TERMINALEQUIPMENT.stationname, INSTITUTION.vn_code, sr.REGDATE\
		    FROM servicerequest AS sr\
		    JOIN SERVICEREQUESTEQPMNTCHECK ON sr.id = SERVICEREQUESTEQPMNTCHECK.requestid\
		    JOIN TERMINALEQUIPMENT         ON sr.equipmentid   = TERMINALEQUIPMENT.id\
		    JOIN INSTITUTION               ON sr.INSTITUTIONID = INSTITUTION.id\
		    WHERE sr.REGYEAR = 2019 and\
                SERVICEREQUESTEQPMNTCHECK.problemdscrptn is not null and\
                sr.INVNUMBER is not null and\
                sr.REGNUM NOT IN (SELECT REGNUM FROM TEMP_TICKETS);"
    fbcursor.execute(select)
    tickets = fbcursor.fetchallmap()
    fbcon.commit()
    fbcursor.execute('DROP TABLE TEMP_TICKETS;')
    fbcon.commit()
    return tickets

def feel_new_tickets(pgcon, pgcursor, new_tickets):
    for ticket in new_tickets:
        insert = "INSERT INTO reports_ticket\
            (ticket, remark, court_id, year, co7_date, died, name, invent_number, serial_number, co7_state, co8_state, co41_state, co42_state, kind, location)\
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;"
        
        pgcursor.execute(insert, (ticket['regnum'], ticket['problemdscrptn'],\
                                ticket['vn_code'], YEAR_NOW, ticket['regdate'].date(), False,\
                                ticket['stationname'], ticket['INVNUMBER'], ticket['SERNUMBER'], 'n', 'n', 'n', 'n','n','c'))    
    pgcon.commit()

def main():
    try:
        pgcon = psycopg2.connect("dbname='repairs' user='postgres' \
                                host='192.168.10.20' password='postgres'")
        pgcursor = pgcon.cursor()
    except Exception as exp:
        print(exp)

    try:
        fbcon = fdb.connect(dsn='192.168.10.10:cia', user='SYSDBA', password='m')
        fbcursor = fbcon.cursor()
    except Exception as exp:
        print(exp)

    tickets = get_tickets(pgcon, pgcursor)
    feel_temp_table(fbcon, fbcursor, tickets)
    new_tickets = get_new_tickets(fbcon, fbcursor)
    feel_new_tickets(pgcon, pgcursor, new_tickets)

    pgcursor.close()
    pgcon.close()
    fbcursor.close()
    fbcon.close()

#main()