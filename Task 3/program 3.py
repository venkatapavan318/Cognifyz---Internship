from datetime import datetime

class Task:
    def __init__(self, task_id, description, status="Pending", due_date=None, priority="Medium"):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.due_date = due_date if due_date else "No due date"  # Optional due date, defaults to "No due date"
        self.priority = priority

    def __str__(self):
        return f"Task ID: {self.task_id}, Description: {self.description}, Status: {self.status}, Due Date: {self.due_date}, Priority: {self.priority}"

    # Update task status
    def update_status(self, new_status):
        self.status = new_status

    # Update task priority
    def update_priority(self, new_priority):
        self.priority = new_priority

    # Update task due date
    def update_due_date(self, new_due_date):
        self.due_date = new_due_date

# Global list to store tasks
task_list = []
next_id = 1  # To track the next available task ID

# Create Task
def create_task():
    global next_id
    print("Enter details for the new task:")

    description = input("Enter task description: ")
    status = input("Enter task status (Pending, In Progress, Completed): ")
    due_date = input("Enter task due date (YYYY-MM-DD) or press Enter to skip: ")
    priority = input("Enter task priority (Low, Medium, High): ")

    # If no due date is entered, set it to None
    due_date = due_date if due_date else None

    # Create new task object
    new_task = Task(next_id, description, status, due_date, priority)

    # Add task to the task list
    task_list.append(new_task)
    print(f"\nTask created successfully with ID: {new_task.task_id}")
    
    # Increment the task ID for the next task
    next_id += 1

# Read and Display Tasks
def read_and_display_tasks():
    print("\n--- All Tasks ---")
    if not task_list:
        print("No tasks available.")
    else:
        for task in task_list:
            print(task)

# Update Task Details
def update_task():
    task_id = int(input("Enter the task ID to update: "))
    task = next((t for t in task_list if t.task_id == task_id), None)
    
    if task:
        print(f"\nCurrent details for Task ID {task_id}:")
        print(task)

        print("\nChoose the detail to update:")
        print("1. Update Status")
        print("2. Update Priority")
        print("3. Update Due Date")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            new_status = input("Enter new status (Pending, In Progress, Completed): ")
            task.update_status(new_status)
            print("Task status updated successfully!")

        elif choice == "2":
            new_priority = input("Enter new priority (Low, Medium, High): ")
            task.update_priority(new_priority)
            print("Task priority updated successfully!")

        elif choice == "3":
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            task.update_due_date(new_due_date)
            print("Task due date updated successfully!")

        else:
            print("Invalid option. No changes made.")
    else:
        print("Task not found.")

# Delete Task
def delete_task():
    task_id = int(input("Enter the task ID to delete: "))
    task = next((t for t in task_list if t.task_id == task_id), None)
    
    if task:
        task_list.remove(task)
        print(f"Task with ID {task_id} has been deleted successfully.")
    else:
        print("Task not found.")

def main():
    while True:
        print("\nTask Manager")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == "1":
            create_task()
        elif option == "2":
            read_and_display_tasks()  # Calling the method to read and display tasks
        elif option == "3":
            update_task()  # Calling the method to update task details
        elif option == "4":
            delete_task()  # Calling the method to delete task
        elif option == "5":
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
