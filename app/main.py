from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world! This is version: 0.0.2'