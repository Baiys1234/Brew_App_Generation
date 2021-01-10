class Drink:
      
    def __init__(self, name, Type, volume): 
        self.name = name
        self.Type = Type
        self.volume = volume
        
    def __repr__(self):
        return f"Drink: {self.name}, Volume: {self.volume}, Type: {self.Type}"