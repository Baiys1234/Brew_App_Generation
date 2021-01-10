import pymysql

connection = pymysql.connect(
    host = "localhost",
    port = 3306, 
    user = "root",
    password = "Cra5hBand1c00t",
    database = "miniproject"
)

mycursor = connection.cursor()

def write_drink_to_database(drink_name, Type, volume):
    sql = "INSERT INTO `drinks` (`drink_name`, `Type`, `volume`) VALUES (%s, %s, %s)"
    val = (drink_name, Type, volume)
    mycursor.execute(sql, val)    
    connection.commit()
    
def write_person_to_database(person_name, age, gender):
    sql = "INSERT INTO `people` (`person_name`, `age`, `gender`) VALUES (%s, %s, %s)"
    val = (person_name, age, gender)
    mycursor.execute(sql, val)
    connection.commit()
    
def write_order_to_database(Person_ID, Drink_ID):
    sql = "INSERT INTO `ROUND` (`Person_ID`, `Drink_ID`) VALUES (%s, %s, %s)"
    val = (Person_ID, Drink_ID)
    mycursor.execute(sql, val)
    connection.commit()

def read_people_from_DB():
    mycursor.execute("SELECT `Person_ID`, `Person_Name`, `age`, `gender` FROM PEOPLE")
    myresult = mycursor.fetchall()
    data = []
    for x in myresult:
        data.append(x)
    return data

def display_people_from_DB():
    mycursor.execute("SELECT `Person_Name`, `age`, `gender` FROM PEOPLE")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(", ".join(x))

def read_drink_from_DB():
    mycursor.execute("SELECT `Drink_ID`, `drink_name`, `Type`, `volume` FROM drinks")
    myresult = mycursor.fetchall()
    data = []
    for x in myresult:
        data.append(x)
    return data

def display_drinks_from_DB():
    mycursor.execute("SELECT `drink_name`, `Type`, `volume` FROM drinks")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(", ".join(x))

def load_people():
    mycursor.execute("SELECT `Person_Name`, `age`, `gender` FROM PEOPLE")
    records = mycursor.fetchall()
    return records

def load_drinks():
    mycursor.execute("SELECT `drink_name`, `Type`, `volume` FROM drinks")
    records = mycursor.fetchall()
    return records

def delete_drink(Drink_ID):
    query = "DELETE FROM `drinks` WHERE Drink_ID = %s"
    mycursor.execute(query, (Drink_ID))
    connection.commit()
    
def delete_person(Person_ID):
    query = "DELETE FROM `people` WHERE Person_ID = %s"
    mycursor.execute(query, (Person_ID))
    connection.commit()
    
def edit_person(Name, Age, Gender, Person_ID):
    mycursor.execute("UPDATE people SET Person_Name = '{}', age = '{}', gender = '{}' WHERE Person_ID = '{}'".format(Name, Age, Gender, Person_ID))
    connection.commit()

def edit_drink(Drink_Name, Type, Volume, Drink_ID):
    mycursor.execute("UPDATE drinks SET Drink_Name = '{}', `Type` = '{}', volume = '{}' WHERE Drink_ID = '{}'".format(Drink_Name, Type, Volume, Drink_ID))
    connection.commit()
    
