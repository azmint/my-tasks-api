from flask import Blueprint

from infrastructure.flask.app_handler import handle
from interface.root.root_controller import RootController
from interface.task.create_task.create_task_controller import CreateTaskController

app_routes = Blueprint("app_routes", __name__)


@app_routes.route("/")
def root():
    """APIルート"""
    return handle(RootController)


@app_routes.route("/task/create/")
def create_task():
    """APIルート"""
    return handle(CreateTaskController)
