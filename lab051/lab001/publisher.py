import os
import time

import redis

password = os.getenv("PASSWORD")

red = redis.StrictRedis('localhost', 6379, charset="utf-8", decode_responses=True, password=password)
channel = 'hello'


def publish():
    red.publish(channel, "world")


def get_subscribe_nums(channel):
    # print(red.pubsub_numsub(channel))
    return red.pubsub_numsub(channel)[0][1]


if __name__ == "__main__":
    while True:
        # publish()
        # time.sleep(3)

        num = get_subscribe_nums(channel)
        print("num=", num)
        time.sleep(3)
