import sys
from sqlalchemy import create_engine, text, Column, Integer, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property as mapped_column
from pgvector.sqlalchemy import Vector

Base = declarative_base()


def lab001():
    """
    Returns:
    """

    password = sys.argv[1]
    engine = create_engine(f'postgresql://postgres:{password}@localhost:5432/lab')
    print(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.execute(text('CREATE EXTENSION IF NOT EXISTS vector'))

    # insert data
    from pgvector.sqlalchemy import Vector

    class Item(Base):
        __tablename__ = 'items'
        id = Column(Integer, primary_key=True)
        embedding = Column(Vector(3))

    item = Item(embedding=[7, 8, 9])
    session.add(item)
    session.commit()
    print("inersted")

    # query by l2 distance
    result = session.execute(select(Item).order_by(Item.embedding.l2_distance([3, 1, 2])).limit(5))
    print(result)
    for row in result:
        item = row[0]
        print(item.id, item.embedding, type(item.embedding))

    # 计算距离
    session = Session()
    try:
        sql = text(f"select embedding <-> '[1,2,3]' as distance,id from items")
        # sql = text(f"select 1 - (embedding <=> '{select_embedding}') as distance,clean_value from repair_shop")
        result = session.execute(sql)
        for row in result:
            print("distance:", row[0], "id:", row[1])
    except:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == '__main__':
    lab001()
