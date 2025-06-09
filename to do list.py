todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {task['task']} [{status}]")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        show_tasks()

    elif choice == '2':
        task_text = input("Enter the new task: ")
        todo_list.append({"task": task_text, "done": False})
        print(f"Task '{task_text}' added.")

    elif choice == '3':
        show_tasks()
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"Task '{removed['task']}' removed.")
        else:
            print("Invalid task number.")

    elif choice == '4':
        show_tasks()
        index = int(input("Enter the number of the task to mark as completed: ")) - 1
        if 0 <= index < len(todo_list):
            todo_list[index]['done'] = True
            print(f"Task '{todo_list[index]['task']}' marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
