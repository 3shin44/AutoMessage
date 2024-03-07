from getFinalRow import getFinalRow
from TextGenerator import generateLINEmessage
from sendMsg import sendLINEMsg
# SERVER LOGGER
from serverLog.serverLogger import logging

# 產生資料並發送
logging.info("Start auto message sender")

# 取得資料
result = getFinalRow()

# 組合成目標格式
textMsg = generateLINEmessage(result)

# 發送
sendLINEMsg(textMsg)