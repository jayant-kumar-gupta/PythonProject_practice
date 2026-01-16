from tabulate import tabulate
import random
import time
import csv
import os

QUESTIONS_FILE = "questions.txt"

def get_next_serial_number():
    """Reads the last serial number from the file and returns the next one."""
    if not os.path.exists(QUESTIONS_FILE):
        return 1
    
    try:
        with open(QUESTIONS_FILE, "r", newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
            if data:
                last_row = data[-1]
                # Ensure the first column is a number
                if last_row and last_row[0].isdigit():
                    return int(last_row[0]) + 1
            return 1
    except Exception:
        return 1

def add_question():
    next_serial_number = get_next_serial_number()

    while True:
        print("-" * 74)
        question = input("Enter question: ").capitalize()
        option1 = input("Enter option1: ").capitalize()
        option2 = input("Enter option2: ").capitalize()
        option3 = input("Enter option3: ").capitalize()
        option4 = input("Enter option4: ").capitalize()
        answer = input("Enter answer(Full Text): ").capitalize() # Asking for full text to match format
        
        # Validation: Verify answer matches one of the options
        options = [option1, option2, option3, option4]
        if answer not in options:
             print("Warning: The answer you typed doesn't match any of the options exactly.")
             confirm = input("Are you sure? (y/n): ")
             if confirm.lower() != 'y':
                 continue

        with open(QUESTIONS_FILE, "a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([next_serial_number, question, option1, option2, option3, option4, answer])
            
        print("Question added successfully..")
        next_serial_number += 1
        
        choice = input("Do you want to add more questions? (y/n): ")
        if choice.lower() != "y":
            break


def view_question():
    if not os.path.exists(QUESTIONS_FILE):
         print("No questions found.")
         return

    with open(QUESTIONS_FILE, "r", newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
        print("-" * 74)
        print(tabulate(data, headers=["SN","Question", "Option1", "Option2", "Option3", "Option4", "Answer"]))
        print("-" * 74)

def delete_question():
    if not os.path.exists(QUESTIONS_FILE):
         print("No questions found.")
         return
         
    with open(QUESTIONS_FILE, "r", newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)

    print("-" * 74)
    print(tabulate(data, headers=["SN", "Question", "Option1", "Option2", "Option3", "Option4", "Answer"]))
    print("-" * 74)
    
    try:
        question_number = int(input("Enter question number (SN) to delete: "))
        
        # Find index in list (SN might not match index if deleted previously, so we search)
        index_to_delete = -1
        for i, row in enumerate(data):
            if row and row[0].isdigit() and int(row[0]) == question_number:
                index_to_delete = i
                break
        
        if index_to_delete != -1:
            del data[index_to_delete]
            
            # Re-write the file with updated Serial Numbers
            with open(QUESTIONS_FILE, "w", newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                for i, row in enumerate(data):
                    row[0] = i + 1 # Reset SN
                    writer.writerow(row)
            print("Question deleted successfully.")
        else:
            print("Question number not found.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")

def game():
    while True: # Game Loop for "Play Again"
        if not os.path.exists(QUESTIONS_FILE):
            print("No questions file found! Ask Admin to add questions.")
            return

        # 1. READ ALL QUESTIONS (Non-destructive)
        with open(QUESTIONS_FILE, "r", newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            all_questions = list(reader)
        
        if not all_questions:
            print("No questions available to play.")
            return

        # 2. SHUFFLE IN MEMORY
        random.shuffle(all_questions)
        
        # 3. SELECT TOP 10 (or fewer)
        num_questions = min(10, len(all_questions))
        game_questions = all_questions[:num_questions]
        
        score = 0
        
        time.sleep(1)
        print(f"You will be asked {num_questions} questions.")
        time.sleep(1)
        print("Lets Go!!!!!!!!!")
        time.sleep(1)
        
        for i, row in enumerate(game_questions):
            # row structure: [SN, Question, opt1, opt2, opt3, opt4, Answer]
            question_text = row[1]
            options_list = row[2:6] # Indices 2, 3, 4, 5
            correct_answer = row[6]
            
            # Map options to A, B, C, D
            option_map = {
                "A": options_list[0],
                "B": options_list[1],
                "C": options_list[2],
                "D": options_list[3]
            }
            
            print("-" * 74)
            print(f"Q{i+1}: {question_text}")
            print(f"A. {option_map['A']}")
            print(f"B. {option_map['B']}")
            print(f"C. {option_map['C']}")
            print(f"D. {option_map['D']}")
            print("-" * 74)
            
            user_choice = ""
            while True:
                user_choice = input("Enter your answer (A/B/C/D): ").upper().strip()
                if user_choice in ["A", "B", "C", "D"]:
                    break
                print("Invalid input. Please enter A, B, C, or D.")
            
            user_answer_text = option_map[user_choice]
            
            # Compare answer (case insensitive strip)
            if user_answer_text.strip().lower() == correct_answer.strip().lower():
                print("-" * 74)
                print("Correct Answer!")
                print("-" * 74)
                score += 1
            else:
                print("-" * 74)
                print(f"Wrong Answer! The correct answer was: {correct_answer}")
                print("-" * 74)
        
        # End of round summary
        print("-" * 74)
        print(f"Your final score is {score}/{num_questions}")
        
        if score == num_questions:
            print("Excellent! Perfect Score!")
        elif score >= num_questions * 0.7:
             print("Good Job!")
        else:
             print("Better luck next time.")
        print("-" * 74)

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            break 

#Main program
def main():
    while True:
        print("\n-------------Welcome to the quiz game-------------")
        print("-" * 74)
        print("1. Admin Mode")
        print("2. Player Mode")
        print("3. Exit")
        print("-" * 74)
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            password = "123"
            key = input("Enter password to login: ")
            if key == password:
                print("Logged in successfully..")
                while True:
                    print("\n" + "-" * 32 + "Admin Mode" + "-" * 31)
                    print("1. Add questions")
                    print("2. View questions")
                    print("3. Delete questions")
                    print("4. Exit Admin Mode")
                    print("-" * 74)
                    
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
                        print("Wrong choice. Enter (1-4).")
            else:
                print("Incorrect Password.")

        elif choice == "2":
             print("\n" + "-" * 32 + "Player Mode" + "-" * 31)
             print("1. Start Quiz")
             print("2. Exit Player Mode")
             print("-" * 74)
             
             choice3 = input("Enter your choice: ")
             if choice3 == "1":
                 game()
             elif choice3 == "2":
                 pass # Just goes back to main menu
                 
        elif choice == "3":
            print("GoodBye!")
            break
        else:
            print("Wrong choice. Enter (1-3).")

if __name__ == '__main__':
    main()