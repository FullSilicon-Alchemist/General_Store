"""
    This Python script allows users to create a bill for products, add products to the bill, remove
    products from the bill, and generate a computer-generated bill record.
    
    :param product: The code you provided seems to be a simple program for managing a shopping bill. The
    `product` variable in the code represents the name of the product that the user enters during the
    program execution. The program then checks if the entered product exists in the product database
    (stored in a JSON file) and
    :return: The `get_product` function is returning the price of the product if it is found in the
    products JSON file. If the product is not found, it will return `None`.
    """
# build-in module
import time
import json
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from termcolor import colored
from os import system,name

# user defined module
from modules.products_manager import product_methods
from modules.bills_record_handler import create_new_record





# functions
def load_products() -> dict[str,int]:
    try:
        with open("data\\products.json","r") as f:
            products = json.load(f)
            return products
    except FileNotFoundError:
        print(colored("Error: Couldn't find the products.json file in data directory.","red"))
    except json.JSONDecodeError:
        print(colored("Error: Couldn't decode the JSON File","red"))
        return {}
        
    


def get_product_price(product):
    try:
        global products
        return products.get(product)
    except: 
        print(colored("Can't find the product","red"))



def remove_product(product):
        global bill,list_products
        price = get_product_price(product)
        if(price != None and product in list_products):
            bill -= price
            list_products = list_products.replace(f"{product:<30}\t{price}","")
        else:
            print(colored("The product is not in the bill","red"))






# variables
bill = 0
list_products = "\n"
shop_name = "Mr.Chips One Stop Shop"
products = load_products()
auto_completion = WordCompleter(list(products.keys()),ignore_case=True)


# main
system('cls' if name == 'nt' else 'clear')
while True:
    product_name = prompt("Enter the name of the product = ",completer=auto_completion).lower().rstrip()


    if(product_name in ["exit","final","end","quit"]):
        break
    elif("remove" in product_name):
        remove_product(product_name.split(" ")[1])
    elif("product" in product_name):
        product_methods()

    elif(product_name in list_products):
        print(colored("The product is already in the bill","red"))
        
    else:
        price = get_product_price(product_name)
        if(price != None):
            bill += price
            list_products += f"{product_name:<30}\t{price}\n"
        else:
            print(colored("The product is not available","red"))
        



if(bill != 0):
    # managing time
    tm = time.localtime()
    date_time = f"{tm.tm_year}-{tm.tm_mon}-{tm.tm_mday} \t {tm.tm_hour}:{tm.tm_min}:{tm.tm_sec}"

    # creating string for bill
    record = f"\n{shop_name:^70}\n{'Products':<30} {'Price':<30}\n{list_products}\nYour Total Bill is {bill}$\n{date_time}\n{'Thankyou for your interest and time':^70}\n{"This is computer generated bill":#^70}"
    system('cls' if name == 'nt' else 'clear')
    print(colored(record,"cyan"))
    create_new_record(record,date_time)
else:
    print("Thanks The program ends")