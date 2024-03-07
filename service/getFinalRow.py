from dbConnect import connectDBandRun

# 取得最後一筆資料
def getFinalRow():
    SQLtemplate = "SELECT * FROM LOGBOOK ORDER BY DBID DESC LIMIT 1"
    return connectDBandRun(SQLtemplate)

