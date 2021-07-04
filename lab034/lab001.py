import os
import pymongo


def main():
    password = os.getenv("password")
    print("password:{}".format(password))

    # client = pymongo.MongoClient("mongodb://localhost:27017/")
    client = pymongo.MongoClient(
        'mongodb://{}:{}@{}:{}/?authSource={}'.format("root", password, "localhost", "27017", "admin"))
    db = client.test_db  # 直接写库名
    k = db.list_collection_names(include_system_collections=True)  # 返回当前库下所有的collection名
    print(k)

    # 插入数据
    mydb = client["runoobdb"]
    mycol = mydb["sites"]

    mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

    x = mycol.insert_one(mydict)
    print(x)
    print(x)


if __name__ == '__main__':
    main()
