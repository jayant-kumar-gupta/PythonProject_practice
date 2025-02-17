class BankAccount:
    def __init__(self, acc_num, acc_name, balance):
        self.acc_num = acc_num
        self.acc_name = acc_name
        self.balance = balance

    def deposit_money(self):
        try:
            amount = int(input("Enter the amount to be deposited: "))
            if amount <= 0:
                print("Deposit amount should be greater than 0.")
            else:
                self.balance += amount
                print("Amount deposited successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdraw_money(self):
        try:
            amount = int(input("Enter the amount to be withdrawn: "))
            if amount > self.balance:
                print(f"Insufficient balance. Current balance is {self.balance}")
            elif amount <= 0:
                print("Withdrawal amount must be greater than 0.")
            else:
                self.balance -= amount
                print("Transaction completed successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def view_balance(self):
        print(f"Your current balance is {self.balance}")


def account_creator():
    while True:
        # Get and validate account number
        acc_num = input("Enter your account number: ").strip()
        if not acc_num.isdigit():
            print("Account number must contain only numbers.")
            continue
        acc_num = int(acc_num)

        # Get and validate name
        while True:
            name = input("Enter your name: ").strip()
            if not name.isalpha():
                print("Name should contain only alphabets. Please try again.")
            else:
                break

        # Get and validate initial balance
        while True:
            try:
                balance = int(input("Enter the initial balance: "))
                if balance <= 0:
                    print("Balance should be greater than 0. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Balance must be a number.")

        # Write account to file
        with open("account.txt", "a") as file:
            file.write(f"{acc_num}: {name} Balance = {balance}\n")
        print("Account created successfully.")

        # Return the created account object
        return BankAccount(acc_num, name, balance)



def teleport_object(account):
    object_list.append(account)
    return object_list


def load_accounts():
    object_list = []
    try:
        with open("account.txt", "r") as file:
            for line in file:
                acc_num, rest = line.split(":")
                name, balance = rest.split("Balance =")
                object_list.append(BankAccount(int(acc_num.strip()), name.strip(), int(balance.strip())))
    except FileNotFoundError:
        pass
    return object_list


def object_creator(object_list, acc_num):
    for obj in object_list:
        if obj.acc_num == acc_num:
            return obj
    return None


def update_file(object_list):
    with open("account.txt", "w") as file:
        for account in object_list:
            file.write(f"{account.acc_num}: {account.acc_name} Balance = {account.balance}\n")


def main():
    global object_list
    object_list = load_accounts()
    print("Welcome to Jayant's Bank.")

    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Balance")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            new_account = account_creator()
            teleport_object(new_account)
        elif choice in ("2", "3", "4"):
            print("Log in to your account.")
            acc_num = input("Enter your account number: ").strip()
            if not acc_num.isdigit():
                print("Invalid account number. Please enter numbers only.")
                continue
            acc_num = int(acc_num)

            account = object_creator(object_list, acc_num)
            if account is None:
                print("Account not found.")
                continue
            if choice == "2":
                account.deposit_money()
            elif choice == "3":
                account.withdraw_money()
            elif choice == "4":
                account.view_balance()
            update_file(object_list)
        elif choice == "5":
            print("Thank you for visiting Jayant's Bank.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    object_list = []  # Initialize global object list
    main()