from flask import Flask
from app import routes


def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

    routes.init_app(app)

    return app