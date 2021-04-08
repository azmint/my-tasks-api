from flask import Blueprint

from infrastructure.flask.app_handler import handle

app_routes = Blueprint("app_routes", __name__)
