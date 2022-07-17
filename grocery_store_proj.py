import orders_data
from product_data import *
from orders_data import *

while True:
    print("1. Insert Products Data")
    print("2. Delete Products Data")
    print("3. View Products Data")
    print("4. Insert Orders Data")
    print("5. Insert Orders_Details")
    print("6. View Orders_Details")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter product_name: ")
        unit = input("Enter unit: ")
        price = input("Enter price: ")
        insert_products(name, unit, price)
    elif choice == 2:
        product_id = input("Enter the id to delete: ")
        delete_products(product_id)
    elif choice == 3:
        get_all_products()
    elif choice == 4:
        customer_name = input("Enter customer_name:")
        total = input("Enter Total: ")
        insert_orders(customer_name, total)
    elif choice == 5:
        order_id = input("Enter Id:")
        insert_order_details(order_id)
    elif choice == 6:
        get_all_orders ()
    elif choice == 7:
        quit()
    else:
        print("Invalid Selection. Please try again")