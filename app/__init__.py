from flask import Flask


app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'app/static'
from app import routes