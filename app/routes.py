from flask import Flask, request, Response
from flask.templating import render_template
from flask import request
from werkzeug.utils import secure_filename
from app import app
import tensorflow as tf
from preprocess import ProcessScan
import os
import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

@app.route('/', methods=['GET', 'POST'])
def home_page():
    path = None
    text = None
    results = [None, None]
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        path = os.path.join(app.config['UPLOAD_PATH'], filename)
        f.save(path)
        process_mod = ProcessScan()
        scan = process_mod.process_scan(path)
        text = "The scan has been processed successfully!"
        model = tf.keras.models.load_model('./3d-img-class-model.h5', compile=False)
        prediction = model.predict(np.expand_dims(scan, axis=0))[0]
        scores = [1 - prediction[0], prediction[0]]
        class_names = ['normal', 'abnormal']
        results = []
        for score, name in zip(scores, class_names):
            results.append("This model is %.2f percent confident that CT scan is %s"% ((100 * score), name))

    return render_template("index.html", path=path, text=text, res1=results[0], res2=results[1])

@app.route('/dev')
def dev_page():
    return render_template("dev.html")
