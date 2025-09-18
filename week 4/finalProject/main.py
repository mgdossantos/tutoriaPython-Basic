# Transform repeated commands into functions (e.g., show menu, add task, list tasks).
# Separate the main code and helper functions.

# Variables to store tasks (starting as empty or with a default value)

import utils
task1 = None
task1Status = None
task2 = None
task2Status = None
task3 = None
task3Status = None
taskCounter = 0

utils.show_menu()
# .strip() ensures the user's input has no leading/trailing spaces,
# making option checks easier.
option = input("Enter the number of the desired option: ").strip()

while option != "3":
    if option == "1":
        utils.view_tasks()

    elif option == "2":
        if taskCounter < 3:
            task_number_to_add = int(input("Which task number do you want to add (e.g., 1, 2, 3)? ").strip())
            new_task = input("Enter the new task: ").strip()
            utils.add_task(task_number_to_add, new_task)
        else:
            print("\nYou've already added the maximum number of tasks (3). Remove one to add another.\n")
    else:
        print("\nInvalid option. Try again.\n")

    utils.show_menu()

    # .strip() ensures the user's input has no leading/trailing spaces,
    # making option checks easier.
    option = input("Enter the number of the desired option: ").strip()

print("\nExiting the program. See you soon!")
