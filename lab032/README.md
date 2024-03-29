# [SQLAlchemy](https://www.sqlalchemy.org/)
安装：`pip install sqlalchemy`

|实验|简介|说明|
|---|---|---|
|lab001|mysql增删改查| |
|lab002|postgres| |
|lab003|raw sql| |
|lab004|创建表| |


## 生成映射代码
安装：`pip install sqlacodegen`
NOTICE：直到20230215，请安装`pip install "SQLAlchemy<2"`，因为从2开始结构改了，但是sqlacodegen还没升级。
### mysql
`pip install mysql-connector`
### postgresql
#### MAC下
 1. `brew install postgresql`
 2. `pip install psycopg2`

### 命令
#### mysql
`sqlacodegen mysql+mysqlconnector://root:123456@localhost:3306/alchemy_lab --outfile gen.py`
#### postgresql
`sqlacodegen postgresql://user:password@127.0.0.1:5432/postgres --outfile=models.py --tables friends`

## orm的class>not JSON serializable
class中加上这段
```python
def as_dict(self):
    return {c.name: getattr(self, c.name) for c in self.__table__.columns}
```

## table

## 参考资料
 - [postgresql的orm](https://www.jb51.net/article/214878.htm)   ,注意需要有主键或者索引，不然不会生成class，只会有table