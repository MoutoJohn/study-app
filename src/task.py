class Task:
    def __init__(self, title, done=False, id):
        self.title = title
        self.done = done
        self.id = id
        
    def mark_done(self):
        self.done = True
    
    def mark_undone(self):
        self.done = False
        
    def __str__(self):
        if self.done:
            return f"[x] {self.title}"
        else:
            return f"[ ] {self.title}"
    