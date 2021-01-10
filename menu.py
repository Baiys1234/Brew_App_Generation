from Controller.menu_functions import menu, clear_screen

from Model.person import Person
from Controller.people_functions import read_people_from_file, read_people_from_db, add_person, display_people, write_people

from Model.drink import Drink
from Controller.drink_functions import read_drinks_from_file, read_drinks_from_db, load_drinks_from_db, add_drink, display_drinks, write_drinks

from Model.order import Order
from Controller.order_functions import create_round, return_order, print_order

from Model.preferences import Preferences
from Controller.preferences_functions import assign_preferences, return_preferences, display_preferences

Exit = False
               
while Exit == False:
    menu()
    menu_choice = int(input("Please make a selection ... "))
    
    if menu_choice == 1:
        clear_screen()
        read_people_from_file()
    
    elif menu_choice == 2:
        clear_screen()
        read_people_from_db()
 
    elif menu_choice == 3:
        clear_screen()        
        write_people()
                 
    elif menu_choice == 4:
        clear_screen()        
        read_drinks_from_file()
        
    elif menu_choice == 5:
        clear_screen()        
        read_drinks_from_db()
    
    elif menu_choice == 6:
        clear_screen()        
        write_drinks()
      
    elif menu_choice == 7:
        clear_screen()
        add_person()
        
    elif menu_choice == 8:
        clear_screen()
        add_drink()
    
    elif menu_choice == 9:  
        clear_screen()
        display_people()
    
    elif menu_choice == 10:
        clear_screen()
        display_drinks()
    
    elif menu_choice == 11: 
        clear_screen()   
        create_round()
        clear_screen()
        print_order()
        
    elif menu_choice == 12:
        clear_screen()
        assign_preferences()
        clear_screen()
        display_preferences()
    
    elif menu_choice == 13: 
        write_people()
        Exit = True 
        print("You've selected exit, goodbye!")
        exit()
    
    else:
        print("Please make a valid selection")
        


