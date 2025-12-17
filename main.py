from todo import add_task, view_tasks, delete_task, load_tasks

load_tasks()

while True:
    print("\n--- TO-DO MENU ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice. Please enter a number between 1 and 4.")
