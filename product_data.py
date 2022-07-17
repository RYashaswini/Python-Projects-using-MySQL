from tabulate import tabulate
from sql_connection import *

def get_all_products():
    res = con.cursor()
    sql = "select product_id, name, unit, price from products"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result, headers=["Product_ID", "Product_Name", "Unit", "Price"]))

def insert_products(name, unit, price):
    res = con.cursor()
    sql = "insert into products (name, unit, price) values (%s,%s,%s)"
    user = (name, unit, price)
    res.execute(sql,user)
    con.commit()
    print("Data inserted successfully")

def delete_products(product_id):
    res = con.cursor()
    sql = "delete from products where product_id=%s"
    user = (product_id,)
    res.execute(sql,user)
    con.commit()
    print("data deleted successfully")
