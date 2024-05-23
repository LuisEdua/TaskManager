class UpdateTaskUseCase:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, task_id, name, completed):
        task = self.task_repository.get_by_id(task_id)
        if task:
            task.name = name
            task.completed = completed
            updated_task = self.task_repository.update(task)
            return updated_task
        return None
