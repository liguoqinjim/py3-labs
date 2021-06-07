from gen import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# 连接mysql，select数据
def demo01_query():
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/alchemy_lab')
    print(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # 得到全部数据
    users = session.query(TUser).all()
    for user in users:
        print(user.id, user.username)

    # 条件查询
    users = session.query(TUser).filter(TUser.username == 'kitty').all()
    for user in users:
        print(user.id, user.username)

    # 只查询某个字段
    rows = session.query(TUser.username).filter(TUser.username == 'kitty').all()
    for row in rows:
        print(row[0])


# 插入数据
def demo02_insert():
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/alchemy_lab')
    print(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # add或者add_all 最后commit
    faker_users = [TUser(username='fakename{}'.format(i)) for i in range(10)]
    session.add_all(faker_users)
    session.commit()


# 更新数据
def demo03_update():
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/alchemy_lab')
    print(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(TUser).get(10)
    print(user.id, user.username)

    # 修改
    user.username = "new_fakename"
    session.add(user)
    session.commit()


# 删除数据
def demo04_delete():
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/alchemy_lab')
    print(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(TUser).get(11)
    print(user.id, user.username)

    # 修改
    session.delete(user)
    session.commit()


if __name__ == '__main__':
    # demo01_query()
    # demo02_insert()
    # demo03_update()
    demo04_delete()
