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


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 识别本地文件
result = client.asr(get_file_content('E:/pr_workspace/1-1导学.wav'), 'wav', 16000, {
    'dev_pid': 1536,
})
print(result)
