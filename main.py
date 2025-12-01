# main.py
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.\n")
    else:
        print("\nYour tasks:")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
        print("")

def main():
    tasks = []
    while True:
        print("=== ToDoList ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            t = input("Enter task: ").strip()
            if t:
                tasks.append(t)
                print("Task added.\n")
            else:
                print("Empty task not added.\n")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                n = input("Enter task number to delete: ").strip()
                if n.isdigit():
                    idx = int(n) - 1
                    if 0 <= idx < len(tasks):
                        removed = tasks.pop(idx)
                        print(f"Removed: {removed}\n")
                    else:
                        print("Invalid number.\n")
                else:
                    print("Please enter a number.\n")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
