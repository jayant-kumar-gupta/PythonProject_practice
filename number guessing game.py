import random
import time


def game(start, end):
    computer_number = random.randint(start, end)
    i = 0
    print("**************\nGame ON!")
    print("***********************************\nYou can always press 'Q' to exit the game at any time.\n***********************************")
    time.sleep(3)
    while True:
        user_number = input(f"Enter any number between {start} and {end}. ")

        if user_number == '':
            print("Cannot hold empty input. Try Again!")
            continue

        elif user_number.upper() == "Q":
            print("!!!!!!!!!!! You Lose !!!!!!!!!!!!!!")
            print(f"You gave up on the correct guess: {computer_number}")
            break

        elif int(user_number) > end:
            print(f"You cannot choose number higher than end number i.e. {end}")
            print("-------------------------------------------------------------------------------------")
            continue

        elif int(user_number) < start:
            print(f"You cannot choose number less than start number i.e. {start}")
            print("-------------------------------------------------------------------------------------")
            continue

        elif int(user_number) > computer_number:
            i += 1
            approach = ((computer_number-(int(user_number)-computer_number))/computer_number)*100
            print(f"Approach Percent = -{round(approach,2)}%")
            print(f"Your guessed number {int(user_number)} is High!")
            print("Try guessing Lower Number")
            print("-------------------------------------------------------------------------------------")
            continue

        elif int(user_number) < computer_number:
            i += 1
            approach = ((computer_number - (computer_number-int(user_number))) / computer_number) * 100
            print(f"Approach Percent = +{round(approach,2)}%")
            print(f"Your guessed number {int(user_number)} is Low!")
            print("Try guessing Higher Number")
            print("-------------------------------------------------------------------------------------")
            continue

        elif int(user_number) == computer_number:
            i += 1
            print("-------------------------------------------------------------------------------------")
            print("!!!!!!!!!!! You Won !!!!!!!!!!!!!!")
            if i<2:
                print(f"An Excellent Guess! You guessed a correct number in just {i} attempt.")
            elif i>=2 and i<=5:
                print(f"A Nice Guess! You guessed a correct number in {i} attempts.")
            elif i>5 and i<=10:
                print(f"A Fair Guess! You guessed a correct number in {i} attempts.")
            else:
                print(f"Guessed but not Fair. You guessed a correct number in {i} attempts.")
            print("-------------------------------------------------------------------------------------")
            break

        else:
            print("Wrong Input. Try Again!")
            print("-------------------------------------------------------------------------------------")




def settings(start,end):
    list1 = []
    if end - (start-1) > 100:
        difficulty = "Very Hard"
    elif end - (start -1) > 50:
        difficulty = "Hard"
    elif end - (start-1) > 30:
        difficulty = "Medium"
    elif end - (start-1) > 10:
        difficulty = "Easy"
    else:
        difficulty = "Very Easy"
    list1.append(start)
    list1.append(end)
    list1.append(difficulty)
    return list1



def main():
    start_num = 1
    end_num = 100
    difficulty = "Hard"
    while True:
        print("---------Welcome to the number guessing game----------")
        print("1. Play game")
        print("2. Exit")
        print("3. Settings")
        match input("Enter your choice (1-3). "):
            case "1":
                game(start_num,end_num)
            case "2":
                print("GoodBye!")
                break
            case "3":
                while True:
                    print("-------------------------------------------------------------------------------------")
                    print("In Settings, You can set the start number and end number.")
                    print(f"Current start number: {start_num}")
                    print(f"Current end number: {end_num}")
                    print(f"Difficulty: {difficulty}")
                    print("-------------------------------------------------------------------------------------")
                    time.sleep(1)
                    print("-------------------------------------------------------------------------------------")
                    print("1. Change start and end number.")
                    print("2. Exit Settings.")
                    match input("Enter your choice. "):
                        case "1":
                            while True:
                                try:
                                    start = int(input("Enter new start number. "))
                                except ValueError:
                                    print("Try Again! You must enter number.")
                                    continue
                                while True:
                                    try:
                                        end = int(input("Enter new end number. "))
                                        break
                                    except ValueError:
                                        print("Try Again! You must enter number.")
                                        print("-------------------------------------------------------------------------------------")
                                if start > end:
                                    print("Try Again! Start number should always be greater than end number.")
                                    print("-------------------------------------------------------------------------------------")
                                    continue
                                elif start == end:
                                    print("Try Again! Start number should not be equal to the end number.")
                                    print("-------------------------------------------------------------------------------------")
                                    continue
                                else:
                                    break
                            new_settings = settings(start,end)
                            start_num = new_settings[0]
                            end_num = new_settings[1]
                            difficulty = new_settings[2]
                            print("----Settings successfully changed.----")
                            print("-------------------------------------------------------------------------------------")
                        case "2":
                            break
                        case _:
                            print("Wrong choice. Enter (1-3). ")
                            print("-------------------------------------------------------------------------------------")

            case _:
                print("Wrong choice. Enter (1-3). ")
                print("-------------------------------------------------------------------------------------")


if __name__ == '__main__':
    main()
