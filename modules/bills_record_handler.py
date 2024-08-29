import os

path = "bills_record\\"

def create_new_record(content:str,time:str) -> None:
    if(os.path.exists(path)):
        time = time.replace(" \t ","_",).replace(":","-")
        with open(f"{path}{time}.txt","w") as f:
            f.write(content)
    else:
        print("The folder doesn't exist.")
