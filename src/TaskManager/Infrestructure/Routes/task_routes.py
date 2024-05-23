from flask import Blueprint
from src.TaskManager.Infrestructure.Controllers import task_controller

task_bp = Blueprint('task_bp', __name__)

task_bp.route('/', methods=['GET'])(task_controller.get_tasks)
task_bp.route('/', methods=['POST'])(task_controller.create_task)
task_bp.route('/<string:id>', methods=['PUT'])(task_controller.update_task)
task_bp.route('/<string:id>', methods=['DELETE'])(task_controller.delete_task)
