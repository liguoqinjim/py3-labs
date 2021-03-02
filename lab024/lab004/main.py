from flask import Flask, request, jsonify
from sklearn.datasets import fetch_california_housing
from sklearn import tree
from sklearn.model_selection import train_test_split
from joblib import dump, load
import traceback

model_directory = 'model'
model_file_name = '%s/model.pkl' % model_directory
model_columns_file_name = '%s/model_columns.pkl' % model_directory

dtr = None


def train_and_save():
    # 读取数据
    housing = fetch_california_housing()
    print("数据shape:")
    print(housing.data.shape)
    print("列名:")
    print(housing.feature_names)
    print("特征值:")
    print(housing.data[:1])
    print("标签值:")
    print(housing.target[:1])

    # 切分训练集和数据集
    data_train, data_test, target_train, target_test = train_test_split(
        housing.data, housing.target, test_size=0.1, random_state=0)

    # 构建决策树
    dtr = tree.DecisionTreeRegressor(random_state=0)
    dtr.fit(data_train, target_train)

    # 查看score
    score = dtr.score(data_test, target_test)
    print("score=", score)
    print(data_train[:1])

    # 保存模型
    dump(dtr, model_file_name)


# 预测
def load_and_predict():
    global dtr
    dtr = load(model_file_name)
    result = dtr.predict([[8.3252, 41., 6.98412698, 1.02380952, 322., 2.55555556, 37.88, 122.23]])
    print(result)


app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    if dtr:
        try:
            json_ = request.json

            prediction = list(dtr.predict(json_["instances"]))
            return jsonify({"prediction": prediction})
        except Exception as e:
            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print('train first')
        return 'no model here'


if __name__ == '__main__':
    # 保存模型
    # train_and_save()

    # 加载模型
    load_and_predict()

    app.run(port=8080)
