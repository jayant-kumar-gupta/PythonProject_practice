import json
import os
from xml.etree.ElementTree import indent

tasks = []

def add_task(title, priority=1):
    tasks.append({"title": title, "priority": priority})

def show_tasks():
    # Use list comprehension here
    return [f"{task['title']} (Priority: {task['priority']})" for task in tasks]

def sort_task():
    sorted_tasks = sorted(tasks, key=lambda x:x["priority"], reverse=True)
    return [f"{task['title']} (Priority: {task['priority']})" for task in sorted_tasks]

def main():
    while True:
        print("1. Add task")
        print("2. Show tasks")
        print("3. Sort tasks")
        print("4. Save/Load tasks from JSON file.")
        print("5. Exit")
        match input("Enter your choice. (1-5) "):
            case "1":
                task = input("Enter any task. ")
                priority = int(input("Enter its priority. "))
                add_task(task, priority)
                print("Task successfully added.")
            case "2":
                print(show_tasks())
            case "3":
                print(sort_task())
            case "4":
                match input("S for save, L for load\nEnter your choice. ").lower():
                    case "s":
                        with open("tasks.json", "w") as file:
                            json.dump(tasks, file, indent=4)
                        print("data successfully written to JSON file.")
                    case "l":
                        with open("tasks.json", "r") as f:
                            data = json.load(f)
                            print(data)
            case "5":
                if os.path.exists("tasks.json"):
                    os.remove("tasks.json")
                print("Exiting...")
                break

if __name__ == '__main__':
    main()