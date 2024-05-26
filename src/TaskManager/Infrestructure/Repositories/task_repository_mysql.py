from src.TaskManager.Domain.Ports.task_port import TaskRepository
from src.TaskManager.Infrestructure.Models.task_model import TaskModel
from src.TaskManager.Domain.Entities.task import Task
from src.DataBase.connection import Base, engine, session_local

class TaskRepositoryMySQL(TaskRepository):
    
    def __init__(self):
        Base.metadata.create_all(bind=engine)
        self.db = session_local()
        
    
    def add(self, task):
        task_model = TaskModel(uuid=task.uuid, name=task.name, completed=task.completed, uploaded=task.uploaded)
        self.db.add(task_model)
        self.db.commit()
        return task_model

    def get_all(self):
        task_models = self.db.query(TaskModel).all()
        return [Task(uuid=task_model.uuid, name=task_model.name, completed=task_model.completed, uploaded=task_model.uploaded) for task_model in task_models]

    def get_by_id(self, task_id):
        task_model = self.db.query(TaskModel).filter(TaskModel.uuid == task_id).first()
        if task_model:
            return Task(uuid=task_model.uuid, name=task_model.name, completed=task_model.completed, uploaded=task_model.uploaded)
        return None

    def update(self, task):
        task_model = self.db.query(TaskModel).filter(TaskModel.uuid == task.uuid).first()
        if task_model:
            task_model.name = task.name
            task_model.completed = task.completed
            self.db.commit()
            return task_model

    def delete(self, task):
        task_model = self.db.query(TaskModel).filter(TaskModel.uuid == task.uuid).first()
        if task_model:
            self.db.delete(task_model)
            self.db.commit()
