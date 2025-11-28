import time
tasks = []
user_name = input("Enter you name ")
age = int(input("Enter your age "))
time.sleep(5)
if(age >= 18):
  while True:
    print("\n To-Do List Menu\n")
    print("1. Add Task\n")
    print("2. View Tasks\n")
    print("3. Delete Task\n")
    print("4. Exit\n")
    print("5.Mark task as done\n")
    user_input = int(input("Enter your choice\t"))
    
    if(user_input == 1):
      task = input("Enter a task :-\t")
      tasks.append(task)
      print("Task Added!")
  
    elif(user_input == 2):
      if(len(tasks) == 0):
        print("No task in the list")
  
      else:
        print("Your Tasks:- ")
        for i in range(len(tasks)):
          print(f"{i+1}.{tasks[i]}")
  
    elif(user_input == 3):
      try:
        task_no = int(input("Enter the task number to delete :- \t"))
        if (1  <= task_no <= len(tasks) ):
          deleted = tasks.pop(task_no - 1)
          print(f"Deleted\t:\t{deleted}")
        else:
          print(f"Please enter a valid input {user_name}")
  
      except:
        print("Enter a valid number")
  
    elif(user_input == 4):
      print("\nThank you for using To-Do List")
      print(f"Have a Good Day\t{user_name}")
      break
  
    elif(user_input == 5):
        try:
            done_no = int(input("Enter task number to mark done: "))
            if 1 <= done_no <= len(tasks):
                tasks[done_no - 1] = f"{tasks[done_no - 1]} \u2705" 
                print("Task marked as completed!")
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input.")
  
    else:
      print("Invalid Input")
else:
  print("You are very young to use this")