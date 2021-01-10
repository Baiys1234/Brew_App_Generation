import os

def menu():
    print("------------------------------------------------------------")
    print("                             Menu")
    print("------------------------------------------------------------")
    print("")
    print("[1] View Contents of People File")
    print("[2] View People in Database")
    print("[3] Add People to File")
    print("[4] View Contents of Drinks File")
    print("[5] View Drinks in Database")
    print("[6] Add Drinks to CSV File")
    print("[7] Add Person")
    print("[8] Add Drinks")
    print("[9] View List of People")
    print("[10] View List of Drinks")
    print("[11] Activate Round")
    print("[12] Preferences")
    print("[13] Exit File")
    print("")
    print("------------------------------------------------------------")
    
def clear_screen():
    os.system("cls")
