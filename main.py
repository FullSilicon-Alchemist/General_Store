import time
import json

from modules.products_manager import product_methods
from modules.bills_record_handler import create_new_record





# functions
def get_product(product):
    try:
        with open("data\\products.json","r") as f:
            products = json.load(f)
            return products[product]
    except: 
        print("Can't find the product")



def remove_product(product):
        global bill,list_products
        price = get_product(product)
        if(price != None and product in list_products):
            bill -= price
            list_products = list_products.replace(f"{product:<30}\t{price}","")
        else:
            print("The product in not in the bill")

# variables
bill = 0
list_products = "\n"
shop_name = "Mr.Chips One Stop Shop"

while True:
    product = input("Enter the name of the product = ").lower()
    if(product in ["exit","final","end","quit"]):
        break
    elif("remove" in product):
        remove_product(product.split(" ")[1])
    elif("product" in product):
        product_methods()

    elif(product in list_products):
        print("The product is already in the bill")
        
    else:
        price = get_product(product)
        if(price != None):
            bill += price
            list_products += f"{product:<30}\t{price}\n"
        



if(bill != 0):
    tm = time.localtime()
    date_time = f"{tm.tm_year}-{tm.tm_mon}-{tm.tm_mday} \t {tm.tm_hour}:{tm.tm_min}:{tm.tm_sec}"

    record = f"\n{shop_name:^70}\n{'Products':<30} {'Price':<30}\n{list_products}\nYour Total Bill is {bill}$\n{date_time}\n{'Thankyou for your interest and time':^70}\n{"This is computer generated bill":#^70}"

    
    print(record)
    create_new_record(record,date_time)
else:
    print("Thanks The program ends")