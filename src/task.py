import uuid

class Task:
    def __init__(self, title, done=False, task_id=None):
        self.title = title
        self.done = done
        self.task_id = task_id if task_id is not None else uuid.uuid4()
        
    def toggle(self):
        self.done = not self.done
        
    def __str__(self):
        if self.done:
            return f"[x] {self.title}"
        else:
            return f"[ ] {self.title}"
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not title.strip():
            raise ValueError("The title cannot be empty.")
        self._title = title
            
    