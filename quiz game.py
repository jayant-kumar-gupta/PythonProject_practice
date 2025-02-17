from tabulate import tabulate
import random
import time

def add_question():
    # Determine the next serial number
    try:
        with open("questions.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1]
                last_serial_number = int(last_line.split(",")[0])
                next_serial_number = last_serial_number + 1
            else:
                next_serial_number = 1
    except FileNotFoundError:
        next_serial_number = 1

    while True:
        print("--------------------------------------------------------------------------")
        question = input("Enter question: ").capitalize()
        option1 = input("Enter option1: ").capitalize()
        option2 = input("Enter option2: ").capitalize()
        option3 = input("Enter option3: ").capitalize()
        option4 = input("Enter option4: ").capitalize()
        answer = input("Enter answer: ").capitalize()
        with open("questions.txt", "a") as file:
            file.write(f"{next_serial_number},{question},{option1},{option2},{option3},{option4},{answer}\n")
        with open("questions2.txt", "a") as file:
            file.write(f"{next_serial_number},{question},{option1},{option2},{option3},{option4},{answer}\n")
        print("Question added successfully..")
        next_serial_number += 1
        choice = input("Do you want to add more questions? (y/n): ")
        if choice == "n":
            break
        elif choice == "y":
            continue
        else:
            print("Wrong Input! Enter y for yes or n for no.")


def view_question():
    with open("questions.txt", "r") as file:
        data = file.readlines()
        data = [line.strip().split(",") for line in data]
        print("--------------------------------------------------------------------------")
        print(tabulate(data, headers=["SN","Question", "Option1", "Option2", "Option3", "Option4", "Answer"]))
        print("--------------------------------------------------------------------------")

def delete_question():
    with open("questions.txt", "r") as file:
        lines_list = file.readlines()
        data = [line.strip().split(",") for line in lines_list]
        print("--------------------------------------------------------------------------")
        print(tabulate(data, headers=["SN", "Question", "Option1", "Option2", "Option3", "Option4", "Answer"]))
        print("--------------------------------------------------------------------------")
        try:
            question_number = int(input("Enter question number to delete: "))
            if 1 <= question_number <= len(lines_list):
                del lines_list[question_number - 1]
                with open("questions.txt", "w") as _file:
                    for i, line in enumerate(lines_list):
                        data = line.strip().split(",")
                        _file.write(f"{i + 1},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]}\n")
                with open("questions2.txt", "w") as _file:
                    for i, line in enumerate(lines_list):
                        data = line.strip().split(",")
                        _file.write(f"{i + 1},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]}\n")
                print("Question deleted successfully.")
            else:
                print("Wrong question number. Enter question number shown in the list.")
        except ValueError:
            print("Question number contains only number.")

def game():
    time.sleep(1)
    print("You will be asked 10 questions. ")
    time.sleep(1)
    print("Each question consists of 1 mark. ")
    time.sleep(2)
    print("Lets Go!!!!!!!!!")
    time.sleep(1)
    with open("questions2.txt", "r") as file:
        lines_list = file.readlines()
        score = 0
        for i in range(10):
            my_dict = {}
            line = random.choice(lines_list)
            data = line.strip().split(",")
            print("--------------------------------------------------------------------------")
            print(f"Q{i+1}: {data[1]}")
            print(f"A. {data[2]}")
            print(f"B. {data[3]}")
            print(f"C. {data[4]}")
            print(f"D. {data[5]}")
            print("--------------------------------------------------------------------------")
            my_dict["A"] = data[2]
            my_dict["B"] = data[3]
            my_dict["C"] = data[4]
            my_dict["D"] = data[5]
            answer = input("Enter your answer: ").upper().strip()
            if my_dict[answer] == data[6]:
                score += 1
                print("--------------------------------------------------------------------------")
                print("Correct Answer")
                print("--------------------------------------------------------------------------")
            else:
                print("--------------------------------------------------------------------------")
                print("Wrong Answer")
                print("--------------------------------------------------------------------------")
            lines_list.remove(line)
            with open("questions2.txt", "w") as _file:
                for line in lines_list:
                    _file.write(line)
    with open("questions.txt", "r") as file:
        lines_list = file.readlines()
        with open("questions2.txt", "w") as _file:
            for line in lines_list:
                _file.write(line)
    while True:
        print("--------------------------------------------------------------------------")
        print("1. Review score. ")
        print("2. Play again. ")
        print("3. Exit. ")
        print("--------------------------------------------------------------------------")
        choice = input("Enter your choice: ")
        print("--------------------------------------------------------------------------")
        if choice == "1":
            print(f"Your score is {score}")
            if score < 5:
                print("Better luck next time.")
                print("--------------------------------------------------------------------------")
            elif score < 8:
                print("Good.")
                print("--------------------------------------------------------------------------")
            else:
                print("Excellent.")
                print("--------------------------------------------------------------------------")
        elif choice == "2":
            game()
        elif choice == "3":
            break
        else:
            print("Wrong choice. Enter (1-3). ")

#Main program

def main():
    while True:
        print("-------------Welcome to the quiz game-------------")
        print("--------------------------------------------------------------------------")
        print("1. Admin Mode")
        print("2. Player Mode")
        print("3. Exit")
        print("--------------------------------------------------------------------------")
        choice = input("Enter your choice: ")
        if choice == "1":
            password = "123"
            key = input("Enter password to login. ")
            if key == password:
                print("Logged in successfully..")
                while True:
                    print("--------------------------------Admin Mode-------------------------------")
                    print("--------------------------------------------------------------------------")
                    print("1. Add questions. ")
                    print("2. View questions. ")
                    print("3. Delete questions. ")
                    print("4. Exit Admin Mode. ")
                    print("--------------------------------------------------------------------------")
                    choice2 = input("Enter your choice: ")
                    if choice2 == "1":
                        add_question()
                    elif choice2 == "2":
                        view_question()
                    elif choice2 == "3":
                        delete_question()
                    elif choice2 == "4":
                        break
                    else:
                        print("Wrong choice. Enter (1-3). ")

        elif choice == "2":
            print("--------------------------------Player Mode-------------------------------")
            print("--------------------------------------------------------------------------")
            print("1. Start Quiz. ")
            print("2. Exit Player Mode. ")
            print("--------------------------------------------------------------------------")
            choice3 = input("Enter your choice: ")
            if choice3 == "1":
                game()
            elif choice3 == "2":
                break
        elif choice == "3":
            print("GoodBye!")
            break
        else:
            print("Wrong choice. Enter (1-3). ")


if __name__ == '__main__':
    main()