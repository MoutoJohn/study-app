from task import Task

class TaskManager:
    def __init__(self):
        self._tasks = {}
    
    def add_task(self, title):
        task = Task(title)        
        self._tasks[task.task_id] = task 
        return task
        
