from flask import Flask
from flask.templating import render_template
from flask import request
from werkzeug.utils import secure_filename
from app import app

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("index.html")

@app.route('/dev')
def dev_page():
    return render_template("dev.html")
