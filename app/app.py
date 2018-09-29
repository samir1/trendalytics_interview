from flask import Flask
from keras.models import load_model
import flask
import numpy as np
from io import BytesIO
from PIL import Image
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
import os
import tensorflow as tf


app = Flask(__name__)
model = None
graph = None


def load_model_and_graph():
    global model
    model = load_model('app/cats_dogs_model.hdf5')

    # save tf graph after loading the model for flask
    global graph
    graph = tf.get_default_graph()
    print('Loaded model')


def prepare_image(image):
    image = image.resize((150, 150))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    return image


@app.route('/')
def hello():
    return "Hey I'm using Docker!"


@app.route('/predict', methods=['POST'])
def predict():
    response = {'success': False}
    if flask.request.method == "POST":
        if flask.request.files.get('image'):
            image = flask.request.files['image'].read()
            image = Image.open(BytesIO(image))
            image = prepare_image(image)

            with graph.as_default():
                preds = model.predict(image)
            response['probability'] = float(preds[0][0])
            response['label'] = 'Dog' if preds[0][0] >= 0.5 else 'Cat'
            response['success'] = True

    return flask.jsonify(response)


if __name__ == '__main__':
    load_model_and_graph()
    app.run(host='0.0.0.0', debug=False, port=5000)

