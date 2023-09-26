from BackEnd import *

for_key()
cust_create_table()
car_create_table()
seller_create_table()
order_create_table()
inventory_create_table()
create_trigger()

customer_add_data('sns1', '1234', 'sns1@some.com', 'bangalore', '1234567890')
customer_add_data('sns2', '12345', 'sns2@some.com', 'bangalore', '1234347890')
customer_add_data('tk1', '1212', 'tk1@some.com', 'kerela', '9876543210')
customer_add_data('tk2', '1313', 'tk2@some.com', 'mumbai', '9876543210')
customer_add_data('tk3', '1313', 'tk3@some.com', 'chennai', '9876543210')

car_add_data(101, 'car1 model1', 45)
car_add_data(102, 'car2 model2', 25)
car_add_data(103, 'car3 model3', 55)
car_add_data(104, 'car4 model4', 35)
car_add_data(105, 'car5 model5', 15)

seller_add_data(321, 'seller1', 'state1', '1111111111')
seller_add_data(322, 'seller2', 'state2', '2222222222')
seller_add_data(323, 'seller3', 'state3', '3333333333')
seller_add_data(324, 'seller4', 'state4', '4444444444')
seller_add_data(325, 'seller5', 'state5', '5555555555')

inventory_add_data(101, 'car1 model1', 321, 5)
inventory_add_data(102,'car2 model2',322,8)
inventory_add_data(103, 'car3 model3', 323, 7)
inventory_add_data(104,'car4 model4',324,9)
inventory_add_data(105, 'car5 model5', 325, 3)

print(inventory_view_all_data())

order_add_data(1, 101, 321, 2)
order_add_data(2, 102, 322, 3)
order_add_data(3, 103, 323, 4)
order_add_data(4, 104, 324, 2)
order_add_data(5, 105, 325, 1)

print(customer_view_all_data())
print(car_view_all_data())
print(seller_view_all_data())
print(order_view_all_data())
print(inventory_view_all_data())
