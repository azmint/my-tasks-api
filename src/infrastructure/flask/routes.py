from flask import Blueprint

from infrastructure.flask.app_handler import handle
from interface.root.root_controller import RootController

app_routes = Blueprint("app_routes", __name__)


@app_routes.route("/")
def root():
    """APIルート"""
    return handle(RootController)
