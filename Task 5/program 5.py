import os

# File to store tasks data
TASK_FILE = 'tasks.txt'

# Function to load tasks from the text file with error handling
def load_tasks():
    tasks = []
    try:
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, 'r') as file:
                for line in file:
                    # Each line is assumed to have the format: ID | name | description | status
                    task_data = line.strip().split(' | ')
                    if len(task_data) == 4:  # Check if line has all 4 parts
                        task = {
                            'id': int(task_data[0]),
                            'name': task_data[1],
                            'description': task_data[2],
                            'status': task_data[3]
                        }
                        tasks.append(task)
        else:
            print(f"Warning: {TASK_FILE} does not exist. Starting with an empty task list.")
    except FileNotFoundError:
        print(f"Error: The file {TASK_FILE} was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file {TASK_FILE}.")
    except Exception as e:
        print(f"An unexpected error occurred while loading tasks: {e}")
    
    return tasks

# Function to save tasks to the text file with error handling
def save_tasks(tasks):
    try:
        with open(TASK_FILE, 'w') as file:
            for task in tasks:
                # Writing tasks in the format: ID | name | description | status
                file.write(f"{task['id']} | {task['name']} | {task['description']} | {task['status']}\n")
    except PermissionError:
        print(f"Error: You do not have permission to write to the file {TASK_FILE}.")
    except Exception as e:
        print(f"An unexpected error occurred while saving tasks: {e}")

# Function to create a new task
def create_task(tasks, task_name, task_description):
    task = {
        'id': len(tasks) + 1,  # Simple task ID based on number of tasks
        'name': task_name,
        'description': task_description,
        'status': 'Not Started'
    }
    tasks.append(task)
    save_tasks(tasks)  # Save tasks to file
    print(f"Task '{task_name}' created successfully!")

# Function to read and display all tasks
def read_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        print(f"ID: {task['id']}, Name: {task['name']}, Description: {task['description']}, Status: {task['status']}")

# Function to update a task by ID
def update_task(tasks, task_id, new_name=None, new_description=None, new_status=None):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        if new_name:
            task['name'] = new_name
        if new_description:
            task['description'] = new_description
        if new_status:
            task['status'] = new_status
        save_tasks(tasks)  # Save tasks to file after update
        print(f"Task {task_id} updated successfully!")
    else:
        print(f"Task with ID {task_id} not found.")

# Function to delete a task by ID
def delete_task(tasks, task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        tasks.remove(task)
        save_tasks(tasks)  # Save tasks to file after deletion
        print(f"Task {task_id} deleted successfully!")
    else:
        print(f"Task with ID {task_id} not found.")

# Main function to run the program
def main():
    tasks = load_tasks()  # Load tasks from file when the program starts
    
    while True:
        print("\nTask Management Menu:")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            create_task(tasks, task_name, task_description)
        elif choice == '2':
            read_tasks(tasks)
        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            new_name = input("Enter new task name (or press Enter to keep current): ")
            new_description = input("Enter new task description (or press Enter to keep current): ")
            new_status = input("Enter new task status (or press Enter to keep current): ")
            update_task(tasks, task_id, new_name or None, new_description or None, new_status or None)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(tasks, task_id)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
