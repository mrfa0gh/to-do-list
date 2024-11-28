import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    """Load tasks from the file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []


def save_tasks(tasks):
    """Save tasks to the file"""
    with open(TASKS_FILE, "w") as file:
        file.writelines([task + "\n" for task in tasks])

def show_tasks(tasks):
    """Display the tasks"""
    if not tasks:
        print("\nNo tasks available!")
    else:
        print("\nCurrent tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task"""
    task = input("\nEnter the new task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task added: {task}")
    else:
        print("Task cannot be empty!")

def remove_task(tasks):
    """Remove a task"""
    show_tasks(tasks)
    try:
        index = int(input("\nEnter the task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def main():
    """Main function"""
    print("Welcome to the To-Do List Manager!")
    tasks = load_tasks()

    while True:
        print("\nChoose an option:")
        print("1. View tasks")
        print("2. Add a new task")
        print("3. Remove a task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
