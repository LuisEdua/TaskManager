from abc import ABC, abstractmethod


class TaskRepository(ABC):
    @abstractmethod
    def add(self, task):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, task_id):
        pass

    @abstractmethod
    def update(self, task):
        pass

    @abstractmethod
    def delete(self, task):
        pass
