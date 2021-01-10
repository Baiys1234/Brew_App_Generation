import os
import sys

from Controller.file_handler import read_csv, write_csv
from Model.dbconn import read_people_from_DB, write_person_to_database, load_people, display_people_from_DB, edit_person, edit_person, delete_person
from Model.person import Person

People = []
Person_Count = []
People_ID = []
Person_Count_and_Person_ID = {}
   
def clear_screen():
    os.system("cls")
    
def read_people_from_file():
    print("------------------------------------------------------------")
    print("                          People CSV")
    print("------------------------------------------------------------")
    print("")
    read_csv("people.csv")
    print("")
    print("------------------------------------------------------------")

def read_people_from_db():
    print("------------------------------------------------------------")
    print("                      People in Database")
    print("------------------------------------------------------------")
    print("")
    display_people_from_DB()
    print("")
    print("------------------------------------------------------------")
    print("")
    print("[1] Edit Person")
    print("[2] Delete a Person")
    print("[3] Load People from Database")
    print("[4] Return to Menu")
    print("")
    
    choice = int(input("Please enter your selection ... ")) 
    print("")
    
    if choice == 1:
    
        clear_screen()
        
        print("------------------------------------------------------------")
        print("                      People in Database")
        print("------------------------------------------------------------")
        
        count_people = 0
        
        People = read_people_from_DB()
             
        for person in People:
            
            count_people += 1
            Person_ID = person[0]  
            
            Person_Count.append(count_people)
            People_ID.append(Person_ID)
            
            print("[" + str(count_people) + "] {}".format(person[1:]).replace('(','').replace(')', ''))
        
        Person_Count_and_Person_ID = dict(zip(Person_Count, People_ID))
        
        print("")
        choice = int(input("Enter the corresponding number for the record you wish to edit."))
        print("")    
        
        if choice in Person_Count_and_Person_ID:
            
            Name = input("Enter your name: ")
            Age = int(input("Enter your age: "))
            Gender = input("Enter your gender: ")  
            Person_ID = Person_Count_and_Person_ID.get(choice)
            
            edit_person(Name, Age, Gender, Person_ID)
            print("Person Altered Successfully!")
            
        else:
            print("Invalid Selection.")    
        
    
    elif choice == 2:
        
        clear_screen()
        
        print("------------------------------------------------------------")
        print("                      People in Database")
        print("------------------------------------------------------------")
        
        count_people = 0
        
        People = read_people_from_DB()
             
        for person in People:
            
            count_people += 1
            Person_ID = person[0]  
            
            Person_Count.append(count_people)
            People_ID.append(Person_ID)
            
            print("[" + str(count_people) + "] {}".format(person[1:]).replace('(','').replace(')', ''))
        
        Person_Count_and_Person_ID = dict(zip(Person_Count, People_ID))
        
        print("")
        choice = int(input("Enter the corresponding number for the record you wish to delete."))
        print("")    
        
        if choice in Person_Count_and_Person_ID:
            
            Person_ID = Person_Count_and_Person_ID.get(choice)
            delete_person(Person_ID)
            print("Person Removed Successfully!")
            
        else:
            print("Invalid Selection.")
    
    elif choice == 3:
        
        load_people_from_db()
    
    print("------------------------------------------------------------")  
    
    if choice == 4:
        clear_screen()
    

def load_people_from_db():
    
    choice = input("Press Y to load table or N to return to the menu. ") 
    
    if choice == "Y" or choice == "y":
        
        records = load_people() 
    
        for row in records: 
              
            Name = row[0]
            Age = row[1]
            Gender = row[2]
            
            person_from_record = Person(Name, Age, Gender)
            People.append(person_from_record)
            
        print("People loaded from Database!")
    
    elif choice == "N" or choice =="n":
        clear_screen()
        
    else:
        print("Please enter a valid selection.")      

def add_person():
    print("------------------------------------------------------------")
    print("                          Add People")
    print("------------------------------------------------------------")
    print("")
    
    count = 5
    
    while count > 0:
    
        print("Please enter " + str(count) + " more records.")
        Name = input("Enter your name: ")
        Age = int(input("Enter your age: "))
        Gender = input("Enter your gender: ")   
        
        person = Person(Name, str(Age), Gender)
        People.append(person)
        
        write_person_to_database(Name, Age, Gender)
        
        count -= 1
        print("User added successfully!")
    
    print("")
    print("------------------------------------------------------------")
       
        
def display_people():
    print("------------------------------------------------------------")
    print("                          People")
    print("------------------------------------------------------------")
    print("")
    for person in People:
        print(person)
    print("")
    print("-------------------------------------------------------------")

    
def write_people():
    people = []
    for p in People:
        people.append([p.name, p.age, p.gender])      
    write_csv("people.csv", people)  
 
