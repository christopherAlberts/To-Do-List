import csv
import os

# File name for the CSV
file_name = 'todo_list.csv'

# Check if file exists, if not create it
if not os.path.isfile(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Task', 'Status'])  # Header


def select_task(tasks):
    while True:
        try:
            print("Enter the number of the task: ")
            task_number = int(input()) - 1
            if 0 <= task_number < len(tasks):
                return tasks[task_number]
            else:
                print("Invalid task number, please try again.")
        except ValueError:
            print("Please enter a valid number.")


def calculate_max_widths():
    max_task_length = max(4, len("Task"))  # Minimum width for "Task"
    max_status_length = max(6, len("Status"))  # Minimum width for "Status"

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            max_task_length = max(max_task_length, len(row[0]))
            max_status_length = max(max_status_length, len(row[1]))

    return max_task_length, max_status_length


def display_tasks():
    max_task_length, max_status_length = calculate_max_widths()

    border_line = f"+-----+{'-' * (max_task_length + 2)}+{'-' * (max_status_length + 2)}+"
    header_line = f"| {'No.':<3} | {'Task':<{max_task_length}} | {'Status':<{max_status_length}} |"

    print(border_line)
    print(header_line)
    print(border_line)

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for index, row in enumerate(reader, start=1):
            print(f"| {index:<3} | {row[0]:<{max_task_length}} | {row[1]:<{max_status_length}} |")

    print(border_line)


def display_tasks_with_numbers():
    max_task_length, max_status_length = calculate_max_widths()

    border_line = f"+-----+{'-' * (max_task_length + 2)}+{'-' * (max_status_length + 2)}+"
    header_line = f"| {'No.':<3} | {'Task':<{max_task_length}} | {'Status':<{max_status_length}} |"

    print(border_line)
    print(header_line)
    print(border_line)

    tasks = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for index, row in enumerate(reader, start=1):
            print(f"| {index:<3} | {row[0]:<{max_task_length}} | {row[1]:<{max_status_length}} |")
            tasks.append(row)

    print(border_line)
    return tasks


def toggle_task_status_ui():
    tasks = display_tasks_with_numbers()
    print("Enter the number of the task to toggle status (or 'x' to return): ")
    task_selection = input()
    if task_selection.lower() == 'x':
        return

    try:
        task_number = int(task_selection) - 1
        if 0 <= task_number < len(tasks):
            task_to_toggle, status = tasks[task_number]
            new_status = 'Incomplete' if status == 'Complete' else 'Complete'

            # Now we need to update this task in the CSV file
            rows = []
            with open(file_name, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == task_to_toggle:
                        row[1] = new_status
                    rows.append(row)

            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            print(f"Task '{task_to_toggle}' marked as {new_status}.")
            display_tasks()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def add_task(task):
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task, 'Incomplete'])


def add_task_ui():
    print("Enter the task to add (or 'x' to return to main menu): ")
    task = input()
    if task.lower() == 'x':
        return
    add_task(task)
    display_tasks()


def edit_task(old_task, new_task):
    rows = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == old_task:
                row[0] = new_task
            rows.append(row)

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def edit_task_ui():
    tasks = display_tasks_with_numbers()
    print("Enter the number of the task to edit (or 'x' to return): ")
    task_selection = input()
    if task_selection.lower() == 'x':
        return

    try:
        task_number = int(task_selection) - 1
        if 0 <= task_number < len(tasks):
            task_to_edit, _ = tasks[task_number]
            print("Enter the new task: ")
            new_task = input()
            edit_task(task_to_edit, new_task)
            display_tasks()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def remove_task(task):
    rows = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != task:
                rows.append(row)

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def remove_task_ui():
    tasks = display_tasks_with_numbers()
    print("Enter the number of the task to remove (or 'x' to return): ")
    task_selection = input()
    if task_selection.lower() == 'x':
        return

    try:
        task_number = int(task_selection) - 1
        if 0 <= task_number < len(tasks):
            task_to_remove, _ = tasks[task_number]
            remove_task(task_to_remove)
            display_tasks()
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


# CLI function
def todo_cli():
    while True:
        print("\nTo-Do List CLI")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Remove Task")
        print("5. Mark Task as Complete")
        print("6. Exit")

        print("Enter your choice: ")
        choice = input()

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task_ui()
        elif choice == '3':
            edit_task_ui()
        elif choice == '4':
            remove_task_ui()
        elif choice == '5':
            # mark_complete_ui()
            toggle_task_status_ui()
        elif choice.lower() in ['6', 'exit', 'x']:
            print("Exiting To-Do List CLI.")
            break
        else:
            print("Invalid choice, please try again.")


# Check if file exists, if not create it
if not os.path.isfile(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Task', 'Status'])  # Header

# Run CLI if the script is run directly
if __name__ == "__main__":
    todo_cli()
