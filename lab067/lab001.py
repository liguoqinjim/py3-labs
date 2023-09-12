import base64
import sys
import urllib
import requests
import os

# 从命令行读取参数

API_KEY = sys.argv[1]
SECRET_KEY = sys.argv[2]


def main():
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate?access_token=" + get_access_token()

    payload = get_file_content_as_base64("/Users/li/Downloads/Snipaste_2023-09-12_22-15-53.jpg", True)

    # image 可以通过 get_file_content_as_base64("C:\fakepath\Snipaste_2023-09-12_22-15-53.jpg",True) 方法获取
    payload = f'image={payload}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)

    # 保存结果到文件
    with open("temp/ocr_result.json", "w") as f:
        f.write(response.text)


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
