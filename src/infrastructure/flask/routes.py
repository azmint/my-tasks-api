from flask import Blueprint

from infrastructure.flask.app_handler import handle

app_routes = Blueprint("app_routes", __name__)


@app_routes.route("/")
def root():
    """APIルート"""
    from interface.root.root_controller import RootController

    return handle(RootController)
