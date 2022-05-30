from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

picture = Flask(__name__)
@picture.route('/')
def picture():
    return 'Is worth a thousand words.'