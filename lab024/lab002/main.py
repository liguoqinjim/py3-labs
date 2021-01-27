import tensorflow as tf
import pandas as pd

print("tensorflow.version:{}".format(tf.__version__))
print("pandas.version:{}".format(pd.__version__))

# 读取数据
data = pd.read_csv("/Volumes/GoogleDrive/我的云端硬盘/workspace/data/tensorflow/Advertising.csv",
                   usecols=['TV', 'radio', 'newspaper', 'sales'])
print(data.head())

# 训练
# 创建模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, input_shape=(3,), activation="relu"),
    tf.keras.layers.Dense(1)
])
model.summary()
model.compile(optimizer="adam", loss="mse")

# 整理数据
x = data.iloc[:, 0:-1]
y = data.iloc[:, -1]
# 测试数据
x_test = data.iloc[:3, 0:-1]
y_test = data.iloc[:3, -1]

model.fit(x, y, epochs=100)
print("x_test:{}".format(x_test))
pred = model.predict(x_test)
print("pred={}".format(pred))
pred2 = model.predict([[230.1, 37.8, 69.2]])
print("pred2={}".format(pred2))

# 保存模型
version = 1
export_path = "../model/model01/{}".format(version)
print('export_path = {}'.format(export_path))

tf.keras.models.save_model(
    model,
    export_path,
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None
)

