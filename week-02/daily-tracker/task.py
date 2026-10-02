class Task:
    def __init__(self, title, completed=False, challenge="", spent_money=0):
        self.title = title
        self.completed = completed
        self.challenge = challenge
        self.spent_money = spent_money
        
    def mark_completed(self):
        self.completed = True
        
    def display(self):
        print(f"{self.title}, {self.completed}, {self.challenge}, {self.spent_money}")
    
