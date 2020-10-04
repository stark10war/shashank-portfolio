import os
from flask import Flask, flash, request, redirect, url_for, session,jsonify, render_template
from werkzeug.utils import secure_filename
from waitress import serve
app = Flask(__name__)
#CORS(app)
@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

@app.route('/deep_ocr_project', methods=['GET'])
def ocr_project():
   return render_template('OCR_project.html')


#app.run()