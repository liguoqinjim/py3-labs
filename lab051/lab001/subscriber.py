import os
import time

import redis

password = os.getenv("PASSWORD")

red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True, password=password)


def subscribe():
    sub = red.pubsub()
    channel = 'hello'
    sub.subscribe(channel)
    for message in sub.listen():
        if message is not None and isinstance(message, dict):
            # username = message.get('data')
            if message['type'] == 'subscribe':
                if message['data'] == 1:
                    print("subscribe success")
            elif message['type'] == 'message':
                print(message['data'])
            else:
                raise ValueError("未定义type")
        # print(message)
        # if message is not None and isinstance(message, dict):
        #     username = message.get('data')


if __name__ == '__main__':
    while True:
        subscribe()

        print("listening...")
        time.sleep(1)
