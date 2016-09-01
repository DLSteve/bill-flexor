from flask import Flask
from config import conf


def create_app():
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(conf)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
