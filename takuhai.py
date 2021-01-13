#!/usr/bin/env python3


import ADC0832
import sys
import time
from datetime import datetime
from linebot import (
    LineBotApi
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


lineuserID = ''
with open('LineAPIuserID.txt') as f:
    lineuserID = f.readline().rstrip('\n')

lineAccessToken = ''
with open('LinechannelAccessToken.txt') as f:
    lineAccessToken = f.readline().rstrip('\n')

line_bot_api = LineBotApi(lineAccessToken)


def init():
    ADC0832.setup()


def loop():
    while True:
        res = ADC0832.getResult() - 80
        if res > 10:
            line_bot_api.push_message(lineuserID, TextSendMessage(text='宅配ボックスが開きました。確認してください。'))
            print("LINE通知を送信しました")
            time.sleep(60)
        else:
            time.sleep(2)

init()
loop()
