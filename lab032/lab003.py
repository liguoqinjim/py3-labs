import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# 连接mysql，select数据
def demo01_query():
    password = sys.argv[1]
    host = sys.argv[2]
    dbname = sys.argv[3]
    engine = create_engine(f'mysql+mysqlconnector://root:{password}@{host}:3306/{dbname}')
    print(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = engine.execute("select * from altcoin")
    print(result)
    names = [row[0] for row in result]
    print(names)


if __name__ == '__main__':
    demo01_query()
