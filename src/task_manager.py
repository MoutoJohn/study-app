from task import Task

class TaskManager:
    def __init__(self):
        self._tasks = {}
    
    def add_task(self, title):
        task = Task(title)        
        self._tasks[task.task_id] = task 
        return task
        
    def remove_task(self, task_id):         #returns an error if fail
        return self._tasks.pop(task_id)     
        
    def get_task(self, task_id):            #returns None if fail
        return self._tasks.get(task_id)     
    
    def get_all_tasks(self):
        return list(self._tasks.values())
    
    def toggle_task(self, task_id):         #returns None if fail
        task = self.get_task(self, task_id)
        if task:
            task.toggle()
        return task