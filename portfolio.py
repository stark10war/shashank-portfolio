import os
from flask import Flask, flash, request, redirect, url_for, session,jsonify, render_template

app = Flask(__name__)
#CORS(app)
@app.route('/', methods=['GET'])
def home():
   return render_template('index.html')

@app.route('/deep_ocr_project', methods=['GET'])
def ocr_project():
   return render_template('OCR_project.html')


#serve(app, host="0.0.0.0", port=80)
