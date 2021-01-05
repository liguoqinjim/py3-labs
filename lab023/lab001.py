from usim800 import sim800
import json


gsm = sim800(baudrate=9600, path="/dev/cu.usbserial-FTA3JNIA")

gsm.sms.send("13764001115","你好世界")