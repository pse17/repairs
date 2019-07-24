import fdb


try:
    con = fdb.connect(dsn='192.168.10.10:cia', user='SYSDBA', password='m')
    cursorfb = con.cursor()
except Exception as exp:
    print('not connect')

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