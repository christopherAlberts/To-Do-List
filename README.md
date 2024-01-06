# To-Do List

![](assets/to_do_list_logo_1.png)

[![Releases](https://img.shields.io/badge/Github-Releases-blue)](https://github.com/christopherAlberts/To-Do-List/releases)
[![Languages](https://img.shields.io/badge/Python-FFD43B?&logo=python&logoColor=blue)](to_do_list.py)
[![OS](https://img.shields.io/badge/Windows-0078D6?&logo=windows&logoColor=white)](README.md) <!--added redme links, just to not go elseweher -->

[//]: # ([![Github All Releases]&#40;https://img.shields.io/github/downloads/Abhijeetbyte/MYPmanager/total?label=Downloads&#41;]&#40;https://github.com/Abhijeetbyte/MYPmanager/releases/download/v1.5/MYPmanager_setup.exe&#41;)

[//]: # ()
[//]: # ([![license]&#40;https://img.shields.io/github/license/abhijeetbyte/MYPmanager&#41;]&#40;LICENSE&#41;)


## Introduction
This To-Do List program is a simple yet effective command-line application for managing your daily tasks. It allows you to add, edit, remove, and toggle the completion status of tasks. Each task's status is clearly marked as either 'Complete' or 'Incomplete'. The program stores all tasks in a CSV file, making it easy to maintain and track your tasks over time.

## Setup
To set up this program, follow these steps:

1. Ensure that Python is installed on your system. This program is compatible with Python 3.x.
2. Save the script as `todo_list.py`.
3. Create an empty CSV file named `todo_list.csv` in the same directory as the script. The program will also create this file automatically if it doesn't exist.

## Usage
Run the script from the command line:

```
python todo_list.py
```

Upon running the script, you will be presented with the following options:

1. **Display Tasks**: View all tasks with their status.
2. **Add Task**: Add a new task to the list.
3. **Edit Task**: Modify an existing task.
4. **Remove Task**: Delete a task from the list.
5. **Toggle Task Status**: Change the status of a task between 'Complete' and 'Incomplete'.
6. **Exit**: Exit the program.

### Examples
- **Add a Task**: Choose option 2, then enter the name of the task.
- **Edit a Task**: Choose option 3, then select the task by its number and enter the new task details.
- **Remove a Task**: Choose option 4, then select the task by its number to remove it.
- **Toggle Task Status**: Choose option 5, then select the task by its number to toggle its completion status.

### Commands
- To return to the main menu at any point, enter 'x'.
- To exit the program, choose option 6 or use `Ctrl+C`.

## Notes
- The tasks are stored in `todo_list.csv` in the format: `Task, Status`.
- The program uses simple file handling and CSV operations for data storage and retrieval.

## License
This To-Do List program is free to use and modify. No license is required.

---

This README provides a clear guide on how to set up and use your To-Do List program. It's formatted in Markdown, which is widely used for README files on platforms like GitHub. You can save this as `README.md` in the same directory as your Python script.