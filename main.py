from classes.product import Product
from classes.inventory import Inventory


shop = Inventory()
shop.add(Product("Pen", 5, 10))
shop.add(Product("Bag", 60, 2))
shop.add(Product("Notebook", 12, 5))


 
shop.find("Pen").sell(4)
shop.find("Bag").add_stock(1)
 
try:
    shop.find("Notebook").sell(50)
except ValueError as error:
    print("error:", error)
 
try:
    pen = Product("Pen", 7, 1)
    shop.add(pen)
except ValueError as error:
    print("error:", error)
 
try:
    shop.find("Bag").price = -3
except ValueError as error:
    print("error:", error)
 
for product in shop.by_value():
    print(product)
print("Total:", shop.total_value)
