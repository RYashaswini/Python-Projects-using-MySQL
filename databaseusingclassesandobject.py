import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="root",database="library_manage")
mycursor=db.cursor()

class data1:
    def insert(self):
        a=int(input("How many rows you have to insert :"))
        for i in range(a):
            id=input("Enter the id")
            name=(input("Enter the name"))
            phno=(input("Enter the Phno"))
            sql1 = "INSERT INTO library (id,name,phno) VALUES ('%s','%s','%s')" % (id,name,phno)
            try:
                mycursor.execute(sql1)
                db.commit()
                print(mycursor.rowcount,"Row Inserted")
            except:
                db.rollback()
                print("Not Row Inserted")
        db.close()

    def read(self):
        mycursor = db.cursor()
        sql2 = "SELECT * FROM library"
        mycursor.execute(sql2)
        result=mycursor.fetchall()
        print(result)
        db.close()

    def delete(self):
        mycursor = db.cursor()
        v = input("Enter the Delete data name ")
        sql4 = "DELETE  FROM library WHERE id='%s'" % v
        try:
            mycursor.execute(sql4)
            db.commit()
            print("deleted")
        except:
            db.rollback()
            print("Not deleted")
        db.close()

    def drop(self):
        mycursor = db.cursor()
        sql5 = "DROP TABLE IF EXISTS library"
        try:
            mycursor.execute(sql5)
            db.commit()
            print("Droped Table")
        except:
            db.rollback()
            print("Not Droped Table")
        db.close()



r = data1()

while True:
    b = int(input("Choose the Data \n (1)ROW Insert \n 2)Read the Data\n 3)Delete \n 4)Drop \n) : "))
    if(b==1):
        r.insert()
    elif(b==2):
        r.read()
    elif(b==3):
        r.delete()
    elif (b == 4):
        r.delete()
    else:
        quit()