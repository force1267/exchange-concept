from flask import Flask

from app.handler import api


app = Flask(__name__)
app.register_blueprint(api)

def run_flask_debug_server():
    app.run(debug=True, host="0.0.0.0", port=8080)
