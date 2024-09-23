# A simple command-line based To-Do List application

class ToDoList:
    def __init__(self):
        self.tasks = []  # List to store tasks

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task['completed'] else "Pending"
                print(f"{i}. {task['task']} - {status}")

    def mark_task_completed(self, task_number):
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number.")
        else:
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as completed.")

    def delete_task(self, task_number):
        if task_number <= 0 or task_number > len(self.tasks):
            print("Invalid task number.")
        else:
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['task']}' deleted.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to mark as completed: "))
            todo_list.mark_task_completed(task_number)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
