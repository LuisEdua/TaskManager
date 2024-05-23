class DeleteTaskUseCase:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def execute(self, task_id):
        task = self.task_repository.get_by_id(task_id)
        if task:
            self.task_repository.delete(task)
            return True
        return False
