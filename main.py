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
    return f'''<html>
    <head>
        {% if title %}
        <title> Главная - Gazon</title>
        {% else %}
        <title>Welcome to Gazon!</title>
    </head>
    <body>
        <h1>Добрый день, {user}!</h1>
    </body>
</html>'''

if __name__ == "__main__":
    app.run()
