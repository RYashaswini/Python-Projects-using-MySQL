from tabulate import tabulate
from sql_connection import *



def insert_orders (customer_name, total):
    res = con.cursor()
    sql = "insert into orders (customer_name, total) values (%s,%s)"
    user = (customer_name, total)
    res.execute(sql,user)
    con.commit()
    print("Data insert Success")

def insert_order_details(order_id, product_id, quantity, total_price):
    res = con.cursor()
    sql = "insert into order_details(order_id, product_id, quantity, total_price) values (%s,%s,%s,%s)"
    user = (order_id, product_id, quantity, total_price)
    res.execute(sql,user)
    con.commit()
    print("Data insert Success")

def get_order_details(order_id):
    res = con.cursor()
    sql = "select * from order_details where order_id = %s"
    sql = "select order_details.order_id, order_detils.quantity, order_details.total_price," \
            "products.name, products.price from order_detils LEFT JOIN products on " \
           "order.details.product_id = products.product_id where order_details.order_id = %s"
    user = (order_id,)
    res.execute(sql,user)
    con.commit()

def get_all_orders ():
    res = con.cursor()
    sql = "Select * from orders"
    res.execute(sql)
    #result = res.fetchone()
    #result = res. fetchmany(2)
    result = res.fetchall()
    #print(result)
    print(tabulate(result,headers=["CUSTOMER_ID","CUSTOMER_Name","Total"]))



