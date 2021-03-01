import pandas as pd
from flask import Flask, request, jsonify
from joblib import dump, load
from sklearn.ensemble import RandomForestClassifier as rf
import traceback

app = Flask(__name__)
model_columns = None
clf = None

model_directory = 'model'
model_file_name = '%s/model.pkl' % model_directory
model_columns_file_name = '%s/model_columns.pkl' % model_directory


def save_model():
    # 读取数据
    df = pd.read_csv('train.csv')
    include = ['Age', 'Sex', 'Embarked', 'Survived']
    df_ = df[include]  # only using 4 variables

    categoricals = []
    for col, col_type in df_.dtypes.iteritems():
        if col_type == 'O':
            categoricals.append(col)
        else:
            df_[col].fillna(0, inplace=True)
    df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)

    # using a random forest classifier (can be any classifier)

    dependent_variable = 'Survived'
    x = df_ohe[df_ohe.columns.difference([dependent_variable])]
    print(x.head())
    y = df_ohe[dependent_variable]
    clf = rf()
    clf.fit(x, y)

    # 保存模型
    dump(clf, model_file_name)

    # 保存模型列
    global model_columns
    model_columns = list(x.columns)
    dump(model_columns, model_columns_file_name)


@app.route("/predict", methods=["POST"])
def predict():
    if clf:
        try:
            json_ = request.json
            query = pd.get_dummies(pd.DataFrame(json_))

            # https://github.com/amirziai/sklearnflask/issues/3
            # Thanks to @lorenzori
            query = query.reindex(columns=model_columns, fill_value=0)

            print("query=", query)
            prediction = list(clf.predict(query))

            # Converting to int from int64
            return jsonify({"prediction": list(map(int, prediction))})

        except Exception as e:

            return jsonify({'error': str(e), 'trace': traceback.format_exc()})
    else:
        print('train first')
        return 'no model here'


if __name__ == '__main__':
    # 保存模型
    # save_model()

    # 加载模型
    clf = load(model_file_name)
    model_columns = load(model_columns_file_name)

    # 运行
    app.run(port=8080)
