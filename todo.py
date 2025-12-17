tasks = []
FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # File will be created later

def save_tasks():
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks()
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks()

    try:
        choice = int(input("Enter task number to delete: "))
        if choice < 1 or choice > len(tasks):
            print("Invalid task number.")
            return

        removed = tasks.pop(choice - 1)
        save_tasks()
        print(f"Removed task: {removed}")

    except ValueError:
        print("Please enter a valid number.")
