from flask import Flask

app = Flask(__name__)


# 路由：第一种方法：修饰器
@app.route('/')
def hello_world():
    return 'Hello World'


# 路由：第二种方法：
def hello_world02():
    return 'Hello World 02'


app.add_url_rule('/hello', '', hello_world02)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=18080, debug=True)
