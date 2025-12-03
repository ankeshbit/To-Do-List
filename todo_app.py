import time

tasks = []

user_name = input("Enter your name: ")

while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError:
        print("Please enter a valid age (numbers only).")

print("Validating age...")
time.sleep(2)

if age < 18:
    print("You are too young to use this application.")
    exit()

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1–5.")
        continue

    if choice == 1:
        task_name = input("Enter the task: ")
        tasks.append({"task": task_name, "done": False})
        print("Task added successfully!")

    elif choice == 2:
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "✔️ Completed" if t["done"] else "❌ Pending"
                print(f"{i}. {t['task']} [{status}]")

    elif choice == 3:
        if not tasks:
            print("Nothing to delete.")
            continue

        try:
            task_no = int(input("Enter task number to delete: "))
            if 1 <= task_no <= len(tasks):
                deleted = tasks.pop(task_no - 1)
                print(f"Deleted: {deleted['task']}")
            else:
                print("Please enter a valid task number.")
        except ValueError:
            print("Invalid number!")

    elif choice == 4:
        if not tasks:
            print("No tasks available to mark done.")
            continue

        try:
            done_no = int(input("Enter task number to mark done: "))
            if 1 <= done_no <= len(tasks):
                tasks[done_no - 1]["done"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input! Enter a number.")

    elif choice == 5:
        print(f"\nThank you for using the To-Do List App, {user_name}! Have a great day ")
        break

    else:
        print("Invalid option! Please choose between 1–5.")
