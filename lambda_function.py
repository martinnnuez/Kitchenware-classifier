#!/usr/bin/env python
# coding: utf-8

import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image
import urllib.request
import io

interpreter = tflite.Interpreter(model_path='kitchen.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']


classes = [
    'cup',
    'fork',
    'glass',
    'knife',
    'plate',
    'spoon'
]

def predict(url):
    with urllib.request.urlopen(url) as url:
        f = io.BytesIO(url.read())

    with Image.open(f) as img:
        img = img.resize((380, 380), Image.NEAREST)
        
    x = np.array(img, dtype='float32')

    X = np.array([x])   

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return dict(zip(classes, float_predictions))


def lambda_handler(event,context):
    url = event['url']
    result = predict(url)
    return result


