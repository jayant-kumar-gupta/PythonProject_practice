from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def add_expense():
    my_dict = {}
    while True:
        section = input("Enter the category of expense. ").capitalize()
        if section.isdigit():
            print("Category cannot contain only numbers.")
            continue
        my_dict["Category"] = section

        while True:
            amount = input("Enter the amount of expense. ")
            if not amount.isdigit():
                print("Amount should contain only numbers.")
                continue
            my_dict["Amount"] = amount
            break

        while True:
            date = input("Enter date (YYYY-MM-DD): ").strip()
            if validate_date(date):
                break
            print("Invalid date format. Please try again.")

        my_dict["Date"] = date

        while True:
            response = input("Want to add expense's description? (y/n). ")
            if response == "y":
                description = input("Enter the expense's description. ").capitalize()
            elif response == "n":
                description = None
            else:
                print("Wrong input! Please enter y for Yes or n for No.")
                continue
            my_dict["Description"] = description
            break

        with open("expense.txt","a") as file:
            for key,value in my_dict.items():
                file.write(f"{key}: {value} ")
            file.write("\n")

        with open("support.txt","a") as file:
            for key,value in my_dict.items():
                file.write(f"{key}: {value}: ")
            file.write("\n")

        print("Detail successfully recorded.")
        print("\n-----------------------------------------------\n")
        break


def view_expense():
    while True:
        print("1. View all expenses")
        print("2. View expenses by category")
        print("3. View expenses by date")
        choice = input("Enter your choice (1-3). ")
        if choice == "1":
            print("\n-----------------------------------------------\n")
            with open("expense.txt","r") as file:
                print(file.read())
            break
        elif choice == "2":
            category = input("Enter the category of expense. ").capitalize()
            print("\n-----------------------------------------------\n")
            print(f"You had the following expense/s in {category}")
            print("\n")
            with open("expense.txt","r") as file:
                for line in file:
                    if f"Category: {category}" in line:
                        print(line)
            break
        elif choice == "3":
            date = input("Enter the date. Format = 'YYYY-MM-DD'. ")
            print("\n-----------------------------------------------\n")
            print(f"You had the following expense/s on {date}")
            print("\n")
            with open("expense.txt","r") as file:
                for line in file:
                    if f"Date: {date}" in line:
                        print(line)
            break
        else:
            print("Wrong input! Please enter (1-3).")


def calculate_expense():
    while True:
        print("1. Calculate total expenses")
        print("2. Calculate total expenses by category")
        choice = input("Enter your choice (1-2): ").strip()
        if choice == "1":
            print("\n-----------------------------------------------\n")
            total = 0
            with open("support.txt", "r") as file:
                for line in file:
                    if "Amount" in line:
                        try:
                            amount = int(line.split(": ")[3])
                            total += amount
                        except (IndexError, ValueError) as e:
                            print(f"Error reading amount from line: {line}. Error: {e}")
            print(f"Total expenses: {total}")
            print("\n-----------------------------------------------\n")
            break
        elif choice == "2":
            category = input("Enter the category of expense: ").capitalize().strip()
            total = 0
            print("\n-----------------------------------------------\n")
            with open("support.txt", "r") as file:
                for line in file:
                    if f"Category: {category}" in line:
                        try:
                            amount = int(line.split(": ")[3])
                            total += amount
                        except (IndexError, ValueError) as e:
                            print(f"Error reading amount from line: {line}. Error: {e}")
            print(f"Total expenses in {category}: {total}")
            print("\n-----------------------------------------------\n")
            break
        else:
            print("Wrong input! Please enter (1-2).")



# Main Program

def main():
    print("\n------------Welcome To Expense Recorder Program------------\n")
    while True:
        print("1. Add expense details. ")
        print("2. View expenses. ")
        print("3. Calculate expenses. ")
        print("4. Exit")
        choice = input("Enter your choice. ")
        if choice == "1":
            print("\n-----------------------------------------------\n")
            add_expense()
        elif choice == "2":
            print("\n-----------------------------------------------\n")
            try:
                open("expense.txt","r")
                view_expense()
            except FileNotFoundError:
                print("Record deleted or File Not Found. No expenses to view.")
        elif choice == "3":
            print("\n-----------------------------------------------\n")
            try:
                open("expense.txt", "r")
                calculate_expense()
            except FileNotFoundError:
                print("Record deleted or File Not Found. No expenses to calculate.")
        elif choice == "4":
            print("\n-----------------------------------------------\n")
            print("GoodBye!")
            break
        else:
            print("Wrong input! Please enter (1-5).")

if __name__ == '__main__':
    main()
