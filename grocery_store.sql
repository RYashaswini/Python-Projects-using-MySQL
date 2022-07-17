create database grocery_store;

use grocery_store;

show databases;

create table products(product_id int not null primary key auto_increment, name varchar(20), unit varchar(20), price int);

select * from products;

create table orders(order_id int not null primary key auto_increment, customer_name varchar(20), total int);

create table order_details(order_id int , product_id int , quantity int, total_price int, foreign key(order_id) references orders(order_id), foreign key (product_id) references products(product_id));

select * from order_details;