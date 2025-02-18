import time


def insert():
    product_name = input("Enter the product name. ").capitalize()
    product_quantity = int(input(f"Enter the quantity of {product_name}."))
    product_price = float(input("Enter price per quantity. "))
    with open("sales.txt","a") as file:
        file.write(f"{product_name}, {product_quantity}, {product_price}\n")
    print("Record added successfully.")
    print("Returning to the main menu... ")
    time.sleep(1)

def view():
    try:
        with open("sales.txt","r") as file:
            product_list = file.readlines()
            if product_list == "":
                print("No data in the file.")
            # else:
            #     for item in product_list:

    except FileNotFoundError:
        print("File missing. No data in the file or Record file may have been deleted.")





def main():
    while True:
        print("1. Enter product details. ")
        print("2. View reports. ")
        print("3. Exit")
        match input("Enter your choice (1-3). "):
            case 1:
                insert()
            case 2:
                view()
            case 3:
                print("GoodBye!")
                return
            case _:
                print("Wrong input! try again.")
                continue