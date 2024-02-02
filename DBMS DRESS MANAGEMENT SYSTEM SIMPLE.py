import os
import platform
import mysql.connector

def create_db():
    d = input("Delete existing 'student' database? (Y/N): ")
    
    if d.upper() == "Y":
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", charset="utf8")
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES LIKE 'student'")
        r = mycursor.fetchone()

        if r:
            mycursor.execute("DROP DATABASE student")
            print("Existing 'student' database dropped.")

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", charset="utf8")
    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE student")
    print("'student' database created.")

    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="student", charset="utf8")
    mycursor = mydb.cursor()

    mycursor.execute("CREATE TABLE IF NOT EXISTS stud (BRANDNUMBER INT, BRANDNAME VARCHAR(255), QTY INT, SIZE VARCHAR(10))")

create_db()

def stuInsert():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="student", charset="utf8")
    mycursor = mydb.cursor()
    B = int(input("Enter the Dress Brand number: "))
    N = input("Enter the Dress brand Name: ")
    Q = int(input("Enter the quantity available in the shop: "))
    S = input("Enter the size(M/L/S/XS/XL/XXL/XXXL) : ")
    mycursor.execute("INSERT INTO stud VALUES (%s, %s, %s, %s)", (B, N, Q, S))
    mydb.commit()

def stuview():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="student", charset="utf8")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM stud")
    r = mycursor.fetchall()
    print("BRANDNUMBER, BRANDNAME, QTY, SIZE")
    for x in r:
        print(x)

def runagain():
    r = input("\nRun Again? (Y/N): ")
    if r.upper() == "Y":
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        MenuSet()
    elif r.upper() == "N":
        exit()
    else:
        print("Enter the right choice")

def MenuSet():
    print("1 : Add new data")
    print("2 : View data")
    print("3 : Exit")
    print("4 : Delete a row from the old data")
    print("5 : Update a row in the new data")
    u = int(input("Select an option from above: "))
    if u == 1:
        stuInsert()
        runagain()
    elif u == 2:
        stuview()
        runagain()
    elif u == 4:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="student", charset="utf8")
        mycursor = mydb.cursor()
        d = int(input("\nEnter the BRANDNUMBER to be deleted"))
        mycursor.execute("DELETE FROM stud WHERE BRANDNUMBER=%s", (d,))
        mydb.commit()
        print("Record deleted successfully")
        runagain()
    elif u == 5:
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="student", charset="utf8")
        mycursor = mydb.cursor()
        v = int(input("\nEnter the BRANDNUMBER to be updated"))
        upd = int(input("\nEnter the QTY to be changed to"))
        mycursor.execute("UPDATE stud SET QTY=%s WHERE BRANDNUMBER=%s", (upd, v))
        print("Record updated successfully")
        mydb.commit()
        runagain()

print("\t\t\tCherry st---->A Dress management system")
print("\t\t\t************************")

MenuSet()

