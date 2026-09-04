import uuid

class Task:
    def __init__(self, title, done=False, task_id=None):
        self.title = title
        self.done = done
        self.task_id = task_id if task_id is not None else uuid.uuid4()
        
    def mark_done(self):
        self.done = True
    
    def mark_undone(self):
        self.done = False
        
    def __str__(self):
        if self.done:
            return f"[x] {self.title}"
        else:
            return f"[ ] {self.title}"
    