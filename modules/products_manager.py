import json



def updated_products(products:dict):
    with open("data\\products.json","w") as f:
            json.dump(products,f)

def product_methods() -> None:
    request = int(input("Press 0 to add a new product\nPress 1 to remove a product\nPress 2 to change the price of the product = "))
    product = input("Enter the name of the  product = ")
    with open("data\\products.json","r") as f:
        products : dict[str,int] = json.load(f)

    if(request == 0):
        # creating new product
        products[product] = int(input(f"Enter the price of {product} = "))
    elif(request in [1,2]):
        try:
            products.get(product)
            if(request == 1):
                # deleting a product
                del products[product]
            else:
                # changing the price of the product
                products[product] = int(input(f"Enter the new price of {product} = "))
        except KeyError:
            print("Product was not found.")
            product_methods()
    else:
        print("Error! Read the instructions carefully.")
        product_methods()
    updated_products(products)