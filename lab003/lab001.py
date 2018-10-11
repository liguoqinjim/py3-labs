# coding:utf8

from aip import AipSpeech
import json

f = open("data/config.json", "rt")
data = json.load(f)
f.close()

""" 你的 APPID AK SK """
APP_ID = data["APP_ID"]
API_KEY = data["API_KEY"]
SECRET_KEY = data["SECRET_KEY"]

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
