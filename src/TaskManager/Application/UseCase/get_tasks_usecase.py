class GetTasksUseCase:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self):
        return self.task_repository.get_all()
