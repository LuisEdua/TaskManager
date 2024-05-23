from src.TaskManager.Domain.Entities.task import Task

class CreateTaskUseCase:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, name, completed=False, uploaded=True):
        new_task = Task(name=name, completed=completed, uploaded=uploaded)
        self.task_repository.add(new_task)
        return new_task
