from os import environ

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def run_flask_debug_server():
    app.run(debug=True)
