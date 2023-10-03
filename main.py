from flask import Flask
import os
user = {'username': 'Miguel'}
# -*- coding: utf-8 -*-
os.environ['FLASK_APP'] = 'main.py'

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'miguel'}
    return '''<html>
    <head>
        <title>{{ Главная }} - Газон</title>
    </head>
    <body>
        <h1>Hello, {{ user.username }}!</h1>
    </body>
</html>'''

if __name__ == "__main__":
    app.run()
