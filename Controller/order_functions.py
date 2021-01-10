import os
import sys

from Model.order import Order

from Controller.people_functions import People
from Controller.drink_functions import Drinks, clear_screen
from Controller.preferences_functions import return_preferences

Person = []
Drink_Selection = []
Completed_Order = {}

def create_round():
    
    print("------------------------------------------------------------")
    print("                          Create Round")
    print("------------------------------------------------------------")
    print("")
    
    Assigned_Preferences = return_preferences()
                                
    for person in People:  
                          
        print("Does {} want a drink?".format(person.name))
        choice = input("Please enter Y to choose their drink, enter N to move onto the next person.")                    
    
        if choice == "Y" or choice == "y":
            
            if person.name in Assigned_Preferences:
                
                preferred_drink = Assigned_Preferences.get(person.name, "")
                print(person.name + " has {} listed as their preference...".format(preferred_drink))
                choice = input("Enter Y to select their preference, enter N to select something different.")  
                
                if choice == "Y" or choice == "y":

                    Person.append(person.name)
                    Drink_Selection.append(preferred_drink)
                    
                elif choice == "N" or choice == "n":
                
                    count = 0 
        
                    for drink in Drinks:
                
                        count += 1               
                        print("[" + str(count) + "] {}".format(drink.name))
                        drink_choice = input("Enter Y to add to the order, enter N to move onto the next selection.")                       
                
                        if drink_choice == "Y" or drink_choice == "y":
            
                            Person.append(person.name)
                            Drink_Selection.append(drink.name)
                            break
                
                        elif drink_choice =="N" or drink_choice == "n": 
                            continue
                
                        else:
                            print("Please enter a valid selection.")
                    
            else: 
                
                count = 0 
        
                for drink in Drinks:
                
                    count += 1               
                    print("[" + str(count) + "] {}".format(drink.name))
                    drink_choice = input("Enter Y to add to the order, enter N to move onto the next selection.")                       
                
                    if drink_choice == "Y" or drink_choice == "y":
            
                        Person.append(person.name)
                        Drink_Selection.append(drink.name)
                        break
                
                    elif drink_choice =="N" or drink_choice == "n": 
                        continue
                
                    else:
                        print("Please enter a valid selection.")
                                                
        elif choice == "N" or choice == "n":
            continue
        
        else:
            print("Please make a valid selection.")
            
def return_order():
    
    temp = Order(Person, Drink_Selection)
    Completed_Order = temp.order
    return Completed_Order
    
def print_order():
        
    print("------------------------------------------------------------")
    print("                          Completed Order")
    print("------------------------------------------------------------")
    print("")
    
    temp = Order(Person, Drink_Selection)
    Completed_Order = temp.order
        
    for person, drink in Completed_Order.items():
        print ("Name: " + person + " Drink: " + drink)
    
    print("")
    print("------------------------------------------------------------")
        
    