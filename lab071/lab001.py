from croniter import croniter
from datetime import datetime


def demo():
    """

    """
    # base = datetime(2010, 1, 25, 4, 46)
    base = datetime.now()

    iter = croniter('*/5 * * * *', base)
    print(iter.get_next(datetime))


if __name__ == '__main__':
    demo()
