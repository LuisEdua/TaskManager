from uuid import uuid4


class Task:
    def __init__(self, name, uploaded=True, completed=False, uuid=None):
        self.uuid = uuid4() if uuid is None else uuid
        self.name = name
        self.completed = False
        self.uploaded = uploaded
