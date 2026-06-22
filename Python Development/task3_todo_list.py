tasks = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task():
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")

def delete_task():
    view_tasks()
    if not tasks:
        return

    choice = input("Enter task number to delete: ").strip()
    if not choice.isdigit():
        print("Please enter a valid number.")
        return

    index = int(choice) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed task: {removed}")
    else:
        print("Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()