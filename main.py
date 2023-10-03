from flask import Flask, render_template
import os
user = {'username': 'Miguel'}
# -*- coding: utf-8 -*-
os.environ['FLASK_APP'] = 'main.py'

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = "Евгений"
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
