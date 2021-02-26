import pandas as pd
from flask import Flask, request, jsonify
from joblib import dump, load
from sklearn.ensemble import RandomForestClassifier as rf


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
    # from sklearn.externals import joblib

    # joblib.dump(clf, 'model.pkl')
    dump(clf, 'model.pkl')

    # 加载模型


app = Flask(__name__)
clf = None


@app.route("/predict", methods=["POST"])
def predict():
    json_ = request.json
    query_df = pd.DataFrame(json_)
    query = pd.get_dummies(query_df)
    prediction = clf.predict(query)
    return jsonify({'prediction': list(prediction)})


if __name__ == '__main__':
    # 加载模型
    clf = load('model.pkl')

    # 运行
    app.run(port=8080)
