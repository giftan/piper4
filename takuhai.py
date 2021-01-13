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
with open('LineAPIuserID') as f:
    lineuserID = f.readline()

LineAccessToken = ''
with open('LinechannelAccessToken') as f:
    lineuserID = f.readline()

line_bot_api = LineBotApi('VfSIblD4ZWXaVtEMNu5ivomf8zo4wxIhAFId9zNyNWfK8Ugl8kic6iFmjehigmGe8VzAZqFI2FbyEBRbfboXFy0TQfNo32cgSjbH7r0sVrvo0w66Bf5XSjb6ok8pb5TcmFyBHov4898dDMXHqftWDgdB04t89/1O/w1cDnyilFU=')


def init():
    ADC0832.setup()


def loop():
    while True:
        res = ADC0832.getResult() - 80
        if res > 10:
            line_bot_api.push_message("U03b44de4864509a4dcc9eeefbe5744ed", TextSendMessage(text='宅配ボックスが開きました。確認してください。'))
            time.sleep(60)
        else:
            time.sleep(2)

init()
loop()
