from tabulate import tabulate
import mysql.connector
con = mysql.connector.connect(host="localhost",user='root',password='root',database='python_db')
'''
if con:
    print("connected")
else:
    print("not connected")
'''

def insert (name, age, city):
    res = con.cursor()
    sql = "insert into user (Name, age, city) values (%s,%s,%s)"
    user = (name, age, city)
    res.execute(sql,user)
    con.commit()
    print("Data insert Success")

def update (name, age, city, id):
    res = con.cursor()
    sql = "update user set name=%s, age = %s, city = %s where id = %s"
    user = (name, age, city, id)
    res.execute(sql, user)
    con.commit()
    print("Data update Success")


def select ():
    res = con.cursor()
    sql = "Select ID, Name, Age, City from user"
    res.execute(sql)
    #result = res.fetchone()
    #result = res. fetchmany(2)
    result = res.fetchall()
    #print(result)
    print(tabulate(result,headers=["ID","Name","Age","City"]))

def delete (id):
    res = con.cursor()
    sql = "delete from user where id=%s"
    user = (id,)
    res.execute(sql, user)
    con.commit()
    print("Data delete Success")

while True:
    print("1. Insert data")
    print("2. Update data")
    print("3. Select data")
    print("4. Delete data")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        city = input("Enter city: ")
        insert(name, age, city)
    elif choice == 2:
        id = input("Enter Id:")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        city = input("Enter city: ")
        update(name, age, city, id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = input("Enter the id to delete: ")
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("Invalid Selection. Please try again")