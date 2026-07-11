class Parent:
    def __init__(self):
        self.parent_balance = 50000
    
    def display_balance(self):
        print(f"Parent's balance is {self.parent_balance}")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_balance = 30000
    
    def display_balance(self):
        print(f"Child's balance is {self.child_balance + self.parent_balance}")

mike = Child()
mike.display_balance()