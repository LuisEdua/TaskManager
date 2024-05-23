from uuid import uuid4


class Task:
    def __init__(self, name, completed=False, uploaded=False, uuid=None):
        self.uuid = uuid4() if uuid is None else uuid
        self.name = name
        self.completed = completed
        self.uploaded = uploaded
