import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *


def lab001():
    """
    读取数据
    :return: 
    """
    username = sys.argv[1]
    password = sys.argv[2]
    engine = create_engine(f'postgresql://{username}:{password}@db_qa:5432/ir_dev')
    print(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # 得到全部数据
    shop_scores = session.query(ShopScore).all()
    for shop_score in shop_scores:
        print(shop_score.id, shop_score.x, shop_score.y, shop_score.version)
        print(shop_score)


def run():
    lab001()
    pass


if __name__ == '__main__':
    run()
