import os
import sys

from Model.preferences import Preferences

from Controller.people_functions import People
from Controller.drink_functions import Drinks
from Controller.menu_functions import menu, clear_screen

Person = []
Drink_Selection = []
Assigned_Preferences = {}

def assign_preferences():
    
    clear_screen()
    
    print("------------------------------------------------------------")
    print("                          Assign Preferences")
    print("------------------------------------------------------------")
    print("")
    
    for person in People:  
        print("Does {} have a preference?".format(person.name))
        choice = input("Please enter Y to choose their drink, enter N to move onto the next person.")             
        
        if choice == "Y" or choice == "y":
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
                                          
        elif choice == "N" or choice == "n":
            continue
        
        else:
            print("Please enter a valid selection")
        
def return_preferences():
    
    temp = Preferences(Person, Drink_Selection)
    Assigned_Preferences = temp.preference
    return Assigned_Preferences

def display_preferences():
    clear_screen()
    print("------------------------------------------------------------")
    print("                          Assign Preferences")
    print("------------------------------------------------------------")
    print("")
    
    temp = Preferences(Person, Drink_Selection)
    Assigned_Preferences = temp.preference
    for person, drink in Assigned_Preferences.items():
        print ("Name: " + person + " Drink: " + drink) 

    print("")
    print("------------------------------------------------------------")
    
    
    