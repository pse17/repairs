import fdb
import psycopg2

try:
    pgcon = psycopg2.connect("dbname='repairs' user='postgres' \
                            host='192.168.10.20' password='postgres'")
    pgcursor = pgcon.cursor()
except Exception as exp:
    print(exp)

try:
    fbcon = fdb.connect(dsn='192.168.10.10:cia', user='SYSDBA', password='m')
    cursorfb = fbcon.cursor()
except Exception as exp:
    print(exp)

select = "SELECT sr.REGNUM\
		    FROM servicerequest AS sr\
		    JOIN SERVICEREQUESTEQPMNTCHECK ON sr.id = SERVICEREQUESTEQPMNTCHECK.requestid\
		    WHERE sr.REGYEAR = 2019 and\
                SERVICEREQUESTEQPMNTCHECK.problemdscrptn is not null and\
                sr.INVNUMBER is not null;"
cursorfb.execute(select)
regnum_list = cursorfb.fetchallmap()
fbcon.commit()

temp_table_create = 'CREATE TABLE tmp_ticket (ticket varchar(6))'
pgcursor.execute(temp_table_create)
pgcon.commit()

for row in regnum_list:
    temp_table_feel = "INSERT INTO tmp_ticket VALUES ('%s')" % row['REGNUM']
    pgcursor.execute(temp_table_feel)    
pgcon.commit()


pgcursor.close()
pgcon.close()

cursorfb.close()
fbcon.close()