from tenacity import *


@retry
def never_gonna_give_you_up():
    print("Retry forever ignoring Exceptions, don't wait between retries")
    raise Exception


@retry(stop=stop_after_attempt(7))
def stop_after_7_attempts():
    print("Stopping after 7 attempts")
    raise Exception


class MyException(Exception):
    pass


@retry(reraise=True, stop=stop_after_attempt(3))
def raise_my_exception():
    print("raise_my_exception")
    raise MyException("Fail")


if __name__ == '__main__':
    # never_gonna_give_you_up()
    # stop_after_7_attempts()

    try:
        raise_my_exception()
    except MyException:
        # timed out retrying
        print("MyException")
        pass
