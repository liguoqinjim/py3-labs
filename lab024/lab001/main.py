import tensorflow as tf
from tensorflow import keras

print('TensorFlow version: {}'.format(tf.__version__))

fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# scale the values to 0.0 to 1.0
train_images = train_images / 255.0
test_images = test_images / 255.0

# reshape for feeding into the model
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print('\ntrain_images.shape: {}, of {}'.format(train_images.shape, train_images.dtype))
print('test_images.shape: {}, of {}'.format(test_images.shape, test_images.dtype))

model = keras.Sequential([
    keras.layers.Conv2D(input_shape=(28, 28, 1), filters=8, kernel_size=3,
                        strides=2, activation='relu', name='Conv1'),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation=tf.nn.softmax, name='Softmax')
])
model.summary()

testing = False
epochs = 2

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=epochs)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print('\nTest accuracy: {}'.format(test_acc))

export_path = "model/hello/1"
print('export_path = {}\n'.format(export_path))

tf.keras.models.save_model(
    model,
    export_path,
    overwrite=True,
    include_optimizer=True,
    save_format=None,
    signatures=None,
    options=None
)

print('\nSaved model:')

# 到model/1目录下
# saved_model_cli show --dir . --all

# 预测
import json

data = json.dumps({"signature_name": "serving_default", "instances": test_images[0:1].tolist()})
print('Data:{}'.format(data))

# docker
# docker run -it --rm -p 8501:8501 -v "/Users/li/Workspace/py3-labs/lab024/lab001/model:/models/test_model" -e MODEL_NAME=test_model tensorflow/serving