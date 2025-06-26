
# To-Do List Project in Python

todo_list = []

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, 1):
            status = "✔️ Done" if task['completed'] else "❌ Not Done"
            print(f"{i}. {task['task']} - {status}")

def add_task():
    task_name = input("Enter task: ")
    task = {"task": task_name, "completed": False}
    todo_list.append(task)
    print("Task added!")

def complete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to mark as complete: "))
        if 1 <= task_no <= len(todo_list):
            todo_list[task_no - 1]['completed'] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(todo_list):
            removed = todo_list.pop(task_no - 1)
            print(f"Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
main()