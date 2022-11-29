import os
import time

import redis

password = os.getenv("PASSWORD")

red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True, password=password)


def publish():
    channel = 'hello'
    red.publish(channel, "world")


if __name__ == "__main__":
    while True:
        publish()
        time.sleep(10)
