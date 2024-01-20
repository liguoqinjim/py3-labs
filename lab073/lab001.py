import requests
import requests


def lab001():
    url = "https://share.proxy.qg.net/pool?key=D5400973&num=1"
    response = requests.get(url)
    data = response.json()
    if data["code"] == "SUCCESS":
        server = data["data"][0]["server"]
        print("server: %s" % data["data"][0]["server"])
    else:
        print(data)
        return

    url = "http://httpbin.org/ip"
    proxies = {
        'http': f'http://{server}',
        'https': f'http://{server}'
    }
    # proxies = {
    #     "http": "http://127.0.0.1:8001",
    #     "https": "http://127.0.0.1:8001",
    # }

    response = requests.get(url, proxies=proxies)
    data = response.json()
    print(data)
    print("Your IP address: %s" % data["origin"])


def lab002():
    """

    """
    proxyUrl = "http://%(user)s:%(password)s@%(server)s" % {
        "user": "5D9E624F",
        "password": "A338B68C426E",
        "server": "tunnel2.qg.net:19552",
    }
    proxies = {
        'http': proxyUrl,
        'https': proxyUrl,
    }

    url = "https://httpbin.org/ip"
    response = requests.get(url, proxies=proxies)
    data = response.json()
    print(data)
    print("Your IP address: %s" % data["origin"])


if __name__ == "__main__":
    # lab001()
    lab002()
