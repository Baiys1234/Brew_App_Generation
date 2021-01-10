class Order:
    
    def __init__(self, Person, Drink_Selection):
        self.Person = Person
        self.Drink_Selection = Drink_Selection 
        self.order = dict(zip(self.Person, self.Drink_Selection))  