class Task:
    def __init__(self, title, done=False, id):
        self.title = title
        self.done = done
        self.id = id
        
    def mark_done(self):
        self.done = True
        