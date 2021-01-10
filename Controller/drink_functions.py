import os
import sys

from Model.drink import Drink
from Controller.file_handler import read_csv, write_csv
from Model.dbconn import read_drink_from_DB, write_drink_to_database, load_drinks, display_drinks_from_DB, edit_drink, delete_drink

Drinks = []
Drinks_From_File = []
temp= []
Drink_Count = []
Drinks_ID = []
Drink_Count_and_Drink_ID = {} 

def clear_screen():
    os.system("cls")
    
def read_drinks_from_file():
    print("------------------------------------------------------------")
    print("                          Drinks CSV")
    print("------------------------------------------------------------")
    print("")
    read_csv("drinks.csv")
    print("")
    print("------------------------------------------------------------")

    
def read_drinks_from_db():
    print("------------------------------------------------------------")
    print("                     Drinks in Database")
    print("------------------------------------------------------------")
    print("")
    display_drinks_from_DB()
    print("")
    print("------------------------------------------------------------")
    print("")
    print("[1] Edit Drink")
    print("[2] Delete a Drink")
    print("[3] Load Drinks from Database")
    print("[4] Return to Menu")
    print("")
    
    choice = int(input("Please enter your selection ... ")) 
    print("")
    
    if choice == 1:
        
        clear_screen()
        
        print("------------------------------------------------------------")
        print("                      Drinks in Database")
        print("------------------------------------------------------------")
        
        count_drinks = 0
        
        Drinks = read_drink_from_DB()
             
        for drink in Drinks:
            
            count_drinks += 1
            Drink_ID = drink[0]  
            
            Drink_Count.append(count_drinks)
            Drinks_ID.append(Drink_ID)
            
            print("[" + str(count_drinks) + "] {}".format(drink[1:]).replace('(','').replace(')', ''))
        
        Drink_Count_and_Drinks_ID = dict(zip(Drink_Count, Drinks_ID))
        
        print("")
        choice = int(input("Enter the corresponding number for the record you wish to edit."))
        print("")    
        
        if choice in Drink_Count_and_Drinks_ID:
            
            Name = input("Enter the drinks name: ")
            Type = input("Enter the drink type: ")
            Volume = input("Enter the volume: ")  
            Drink_ID = Drink_Count_and_Drinks_ID.get(choice)
            
            edit_drink(Name, Type, Volume, Drink_ID)
            print("Drink Altered Successfully!")
            
        else:
            print("Invalid Selection.")    
    
    elif choice == 2:
        
        clear_screen()
        
        print("------------------------------------------------------------")
        print("                      Drinks in Database")
        print("------------------------------------------------------------")
        
        count_drinks = 0
        
        Drinks = read_drink_from_DB()
             
        for drink in Drinks:
            
            count_drinks += 1
            Drink_ID = drink[0]  
            
            Drink_Count.append(count_drinks)
            Drinks_ID.append(Drink_ID)
            
            print("[" + str(Drink_Count) + "] {}".format(drink[1:]).replace('(','').replace(')', ''))
        
        Drink_Count_and_Drink_ID = dict(zip(Drink_Count, Drinks_ID))
        
        print("")
        choice = int(input("Enter the corresponding number for the record you wish to delete."))
        print("")    
        
        if choice in Drink_Count_and_Drink_ID:
            
            Drink_ID = Drink_Count_and_Drink_ID.get(choice)
            delete_drink(Drink_ID)
            print("Drink Removed Successfully!")
            
        else:
            print("Invalid Selection.")
    
    elif choice == 3:
        load_drinks_from_db()
            
    print("------------------------------------------------------------") 
    
    if choice == 4:
        clear_screen()
        
def load_drinks_from_db():
    
    choice = input("Press Y to load table or N to return to the menu. ") 
    
    if choice == "Y" or choice == "y":
        
        records = load_drinks()
        
        for row in records:
            Name = row[0]
            Type = row[1]
            Volume = row[2]
            
            drink_from_record = Drink(Name, Type, Volume)
            Drinks.append(drink_from_record)
                       
        print("Drink selection loaded from Database!")
    
    elif choice == "N" or choice =="n":
        clear_screen()
        
    else:
        print("Please enter a valid selection.")


def add_drink():
    print("------------------------------------------------------------")
    print("                          Add Drinks")
    print("------------------------------------------------------------")
    print("")
    
    count = 5
    
    while count > 0:
        
        print("Please enter " + str(count) + " more records.")
        
        Drink_Name = input("Enter the name of the drink: ")
        Drink_Volume = input("Enter the measurement: ")
        Drink_Type = input("Enter the type: ")
    
        drink = Drink(Drink_Name, Drink_Volume, Drink_Type)
        Drinks.append(drink)
    
        write_drink_to_database(Drink_Name, Drink_Volume, Drink_Type)     
    
        count -= 1
    
        print("Drink added successfully!")
    print("")
    print("------------------------------------------------------------")
 
def display_drinks():
    print("------------------------------------------------------------")
    print("                          Drinks")
    print("------------------------------------------------------------")
    print("")
    for drink in Drinks:
        print(drink)
    print("")
    print("------------------------------------------------------------")

def write_drinks():
    print("------------------------------------------------------------")
    print("                          Drinks")
    print("------------------------------------------------------------")
    print("")
    user_choice = input("Write drinks to file?")
    if user_choice == 'Y' or user_choice == 'y':
        drinks = []
        for d in Drinks:
            drinks.append([d.name, d.volume, d.Type])
        
        write_csv("drinks.csv", drinks)  