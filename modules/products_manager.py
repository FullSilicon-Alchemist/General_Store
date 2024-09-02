import json
from termcolor import colored


def updated_products(products:dict):
    with open("data\\products.json","w") as f:
            json.dump(products,f)

def product_methods() -> None:
    request = int(input("Press 0 to add a new product\nPress 1 to remove a product\nPress 2 to change the price of the product = "))
    product = input("Enter the name of the  product = ")
    with open("data\\products.json","r") as f:
        products : dict[str,int] = json.load(f)

    try:
        if(request == 0):
            #creating new product
            products[product] = int(input(f"Enter the price of {product} = "))
            updated_products(products)
        elif(request == 1):
            #deleting a product
            products.get(product)
            del products[product]
            updated_products(products)
        elif(request == 2):
             #changing the price of the product
             products.get(product)
             products[product] = int(input(f"Enter the new price of {product} = "))
             updated_products(products)
        else:
            print(colored("Error! Read the instructions carefully.","red"))
            product_methods()   
    except ValueError:
         print(colored("Please Enter a number","red"))  
         product_methods()
    except KeyError:
         print(colored("Product was not found.","red"))
         product_methods()
