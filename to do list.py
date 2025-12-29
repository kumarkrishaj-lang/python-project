tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        show_tasks()
        index = int(input("Enter task number to delete: "))
        if 0 < index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number!")
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")
