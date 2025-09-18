def show_menu():
    print("===================================")
    print(" Welcome to the Task Manager ")
    print("===================================\n")

    print("Choose an option:")
    print("1 - View tasks")
    print("2 - Add task")
    print("3 - Exit")

def add_task(task_number, description):
    """Adds a task to a specific variable."""
    print("\n--- Your Tasks ---")
    "Check if there is a task to be displayed"
    if task_number == 1:
        global task1
        task1 = description
        print("1.", task1)
    if task_number == 2:
        global task2
        task2 = description
        print("2.", task2)
    if task_number == 3:
        global task3
        task3 = description
        print("3.", task3)


def view_tasks():
    """Displays the tasks stored in variables."""
    print("\n--- Your Tasks ---")
    if task1:
        print(f"1. {task1}")
    if task2:
        print(f"2. {task2}")
    if task3:
        print(f"3. {task3}")
    # Add more ifs to display additional tasks
    if not task1 and not task2 and not task3:
        print("No tasks added yet.")
    print("--------------------\n")
