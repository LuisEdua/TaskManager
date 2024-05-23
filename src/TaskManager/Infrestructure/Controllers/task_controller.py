from flask import request, jsonify
from src.TaskManager.Application.UseCase.create_task_usecase import CreateTaskUseCase
from src.TaskManager.Application.UseCase.delete_task_usecase import DeleteTaskUseCase
from src.TaskManager.Application.UseCase.get_tasks_usecase import GetTasksUseCase
from src.TaskManager.Application.UseCase.update_task_usecase import UpdateTaskUseCase
from src.TaskManager.Infrestructure.Repositories.task_repository_mysql import TaskRepositoryMySQL

task_repository = TaskRepositoryMySQL()

def get_tasks():
    use_case = GetTasksUseCase(task_repository)
    tasks = use_case.execute()
    return jsonify([{'id': task.uuid, 'name': task.name, 'completed': task.completed, "uploaded": task.uploaded} for task in tasks])

def create_task():
    data = request.get_json()
    use_case = CreateTaskUseCase(task_repository)
    new_task = use_case.execute(name=data['name'], completed=data.get('completed', False), uploaded=data.get('uploaded', False))
    return jsonify({'id': new_task.uuid, 'name': new_task.name, 'completed': new_task.completed, "uploaded": new_task.uploaded}), 201

def update_task(id):
    data = request.get_json()
    use_case = UpdateTaskUseCase(task_repository)
    updated_task = use_case.execute(task_id=id, name=data['name'], completed=data.get('completed', False))
    if updated_task:
        print(updated_task.uploaded)
        return jsonify({'id': updated_task.uuid, 'name': updated_task.name, 'completed': updated_task.completed, 'uploaded': updated_task.uploaded})
    else:
        return jsonify({'error': 'Task not found'}), 404

def delete_task(id):
    use_case = DeleteTaskUseCase(task_repository)
    if use_case.execute(task_id=id):
        return '', 204
    else:
        return jsonify({'error': 'Task not found'}), 404
