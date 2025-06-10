tasks = []

while True:
    print("1. Add tasks")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == '2':
        if not tasks:
            print("No tasks yet.")
        else:
            print("Tasks:")
            for i, task in enumerate(tasks):
                print(i, task)

    elif choice == '3':
        if tasks:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Removed task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
           
            print("No tasks to remove.")

    elif choice == '4':
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
