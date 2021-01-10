class Person:
    
    def __init__(self, name, age, gender): 
        self.name = name
        self.age = age
        self.gender = gender
    
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"