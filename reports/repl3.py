import fdb
import psycopg2


def get_devices(pgcon, pgcursor):
    select = "SELECT invent_number, serial_number FROM reports_device"
    pgcursor.execute(select)
    devices = pgcursor.fetchall()
    pgcon.commit()
    return devices


def feel_temp_table(fbcon, fbcursor, devices):
    temp_table_create = "CREATE GLOBAL TEMPORARY table TEMP_DEVICE (\
        INVNUMBER varchar(20), SERNUMBER varchar(24))\
        ON COMMIT PRESERVE ROWS"
    fbcursor.execute(temp_table_create)

    for inv, serial in devices:
        if inv is not None:
            fbcursor.execute("INSERT INTO TEMP_DEVICE VALUES ('%s','%s')" % (inv, serial))
    fbcon.commit()

def get_new_devices(fbcon, fbcursor):
    select = "SELECT sr.INVNUMBER, sr.SERNUMBER,TERMINALEQUIPMENT.stationname\
        FROM servicerequest AS sr\
        JOIN TERMINALEQUIPMENT ON sr.equipmentid = TERMINALEQUIPMENT.id\
        WHERE SERNUMBER NOT IN\
        (SELECT SERNUMBER FROM TEMP_DEVICE);"
    fbcursor.execute(select)
    device = fbcursor.fetchallmap()
    fbcon.commit()
    return device


def feel_new_devices(pgcon, pgcursor, new_devices):
    for device in new_devices:
        pgcursor.execute("INSERT INTO reports_device (name,invent_number,)\
                             VALUES ('%s','%s','%s')"\
                             % (device[''], device[''], device[''])
    pass

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

    devices = get_devices(pgcon, pgcursor)
    feel_temp_table(fbcon, fbcursor, devices)
    new_devices = get_new_devices(fbcon, fbcursor)
    feel_new_devices(pgcon, pgcursor, new_devices)

    pgcursor.close()
    pgcon.close()
    fbcursor.close()
    fbcon.close()