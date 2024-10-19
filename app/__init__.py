from flask import Flask
from .api.hello import hello_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(hello_bp)

    return app
