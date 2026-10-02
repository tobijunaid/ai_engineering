import json
from task import Task
from pathlib import Path

current_dir = Path(__file__).parent
file_path = Path(__file__).parent / "tasks.txt"

tasks = []

def save_tasks(tasks):
    data = []
    
    for task in tasks:
        data.append({
            "title": task.title,
            "completed": task.completed,
            "challenge": task.challenge,
            "spent_money": task.spent_money
        })
    
    with open(file_path, "w") as file :  
        json.dump(data, file, indent=4)

def load_tasks():
    if not file_path.exists():
        return []

    with open(file_path, "r") as file:
        data = json.load(file)

    tasks = []

    for item in data:
        task = Task(
            item["title"],
            item["completed"],
            item["challenge"],
            item["spent_money"]
        )
        tasks.append(task)

    return tasks

def mark_completed(tasks):
    if not tasks:
        print("No tasks available")
        return
    
    print("\nSelect a task to complete: ")
    
    #Display numbered tasks
    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task.title}")

    choice = input("Enter task number: ")

    #Validating User's choice
    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(tasks):
        print("Task number does not exist.")
        return

    #Selecting the task
    selected_task = tasks[choice - 1]
    selected_task.mark_completed() #Completing and saving

    save_tasks(tasks)
    print("Task marked as completed!")

def record_details(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nSelect a task:")

    for number, task in enumerate(tasks, start=1):
        print(f"{number}. {task.title}")

    choice = input("Enter task number: ")

    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(tasks):
        print("Task number does not exist.")
        return

    selected_task = tasks[choice - 1]

    selected_task.challenge = input(
        "What challenges did you encounter? "
    )

    while True:
        try:
            amount = float(input("How much did you spend? ₦"))
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            selected_task.spent_money = amount
            break
        except ValueError:
            print("Please enter a valid amount.")

    save_tasks(tasks)
    print("Task details updated successfully!")

def daily_summary(tasks):
    total_tasks = len(tasks)
    completed_tasks = [task for task in tasks if task.completed]
    total_spent = sum(task.spent_money for task in tasks)
    pending_task = [task for task in tasks if not task.completed]

    print("\n===== DAILY SUMMARY =====")
    print(f"Total tasks: {len(tasks)}")
    print(f"Total tasks completed: {len(completed_tasks)}")
    print(f"Pending: {len(pending_task)}")
    print(f"Total money spent: ₦{total_spent:.2f}")
    print("==========================\n")
    print("\nChallenges encountered:")
    
    for task in tasks:
        if task.challenge.strip():
            print(f"- {task.challenge}")
            print("==========================\n")

tasks = load_tasks()

while True:
    print("\n===== DAILY TRACKER =====") 
    print("1. Add a task")  
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Record challenge and spending")  
    print("5. Print Daily Summary")
    print("6. Exit\n")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        title = input("Enter task title: ")
        new_task = Task(title)
        tasks.append(new_task)
        save_tasks(tasks)
        print("Task added successfully!")
        
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            for task in tasks:
                task.display()        
    
    elif choice == "3":
        mark_completed(tasks)
    
    elif choice == "4":
        record_details(tasks)
        
    elif choice == "5":
        daily_summary(tasks)
    
    elif choice == "6":
        print("Goodbye")
        break
    
    else:
        print("Invalid options. Please try again.")    
