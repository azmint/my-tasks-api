from flask import Flask

from infrastructure.flask.routes import app_routes
from infrastructure.injector.injector_facade import create_injector


def create() -> Flask:
    """Flackアプリケーションを作成する。"""
    create_injector()
    application = Flask("flask-api")

    application.register_blueprint(app_routes)

    return application
