"""
Developed on Sat July 03 2021

@author: RAJESH KUMAR
"""

#importing all necessary libraries
from __future__ import division, print_function

import os
import re
import glob
import numpy as np
import sys
import cv2



from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename




app = Flask(__name__)

MODEL_PATH = 'VehicleClassifier-model.h5'

# Loading the Vehicle classifier model
model = load_model(MODEL_PATH)


def predict(imgpath, model):
    #reading the file using specific image path
    img = cv2.imread(imgpath)

    #resizing it since our model got trained wrt to 224,224 image size.
    img = cv2.resize(img,(224, 224))
    #img = image.copy()

    # Preprocessing the image

    img_array = image.img_to_array(img)
    # x = np.true_divide(x, 255)

    ## Performing Scaling operation
    img_array = img_array / 255
    preprocessed_image = np.expand_dims(img_array, axis=0)

    preds = model.predict(preprocessed_image)
    preds = np.argmax(preds, axis=1)
    if preds == 0:
        preds = "The Car is Hatchback"
    elif preds == 1:
        preds = "The Car is Multi Ulility Vehicle"
    elif preds == 3:
        preds = "The Car is Sedan"
    elif preds == 4:
        preds = "The Car is SUV"
    else:
        preds = "The Car is not recognized/Does not belong to any of the category {Hatchback, suv, muv, sedan}"

    return preds


@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the image from post request
        f = request.files['file']

        # Save the image to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        f.close()

        # Make prediction
        preds = predict(file_path, model)
        result = preds
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)
