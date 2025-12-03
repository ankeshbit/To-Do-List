# 📝 CLI To-Do List Manager

A Python-based Command Line Interface (CLI) application that helps users manage their daily tasks efficiently. This project demonstrates core programming concepts including data structures, error handling, and user input validation.

## 🚀 Features

* **User Validation:** Secure-feel login with name input and age verification (Users must be 18+).
* **Task Management:**
    * **Add Tasks:** Quickly append new items to your list.
    * **View Tasks:** See all tasks with visual status indicators (✔️/❌).
    * **Mark as Done:** Update task status to completed.
    * **Delete Tasks:** Remove unwanted items from the list.
* **Robust Error Handling:** Prevents crashes when invalid numbers or data types are entered.
* **Interactive Interface:** specific delays (`time.sleep`) to simulate processing and improve user experience.

## 🛠️ Built With

* **Language:** Python 3.x
* **Libraries:** `time` (Standard Library)

## 💻 How to Run

1.  **Prerequisites:** Ensure you have Python installed on your machine.
    ```bash
    python --version
    ```

2.  **Download:** Save the script as `todo_app.py`.

3.  **Run the Application:** Open your terminal or command prompt and run:
    ```bash
    python todo_app.py
    ```

## 📸 Usage Example

```text
Enter your name: Ankesh
Enter your age: 20
Validating age...

===== TO-DO LIST MENU =====
1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Done
5. Exit

Enter your choice: 1
Enter the task: Finish Python Project
Task added successfully!