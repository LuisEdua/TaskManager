from src.TaskManager.Domain.Entities.task import Task

class CreateTaskUseCase:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, name):
        new_task = Task(name)
        self.task_repository.add(new_task)
        return new_task
