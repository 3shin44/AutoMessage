from authConfig import authConfig
import requests

# SERVER LOGGER
from serverLog.serverLogger import logging

def sendLINEMsg(message):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {authConfig['LINE_TOKEN']}"
    }
    data = {
        "to": authConfig['user_id'],
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }
    response = requests.post(url, headers=headers, json=data)

    # Configure logging
    logging.info(response)
