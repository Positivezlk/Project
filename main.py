from flask import Flask
import os

os.environ['FLASK_APP'] = 'main.py'

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()