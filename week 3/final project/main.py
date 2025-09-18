# Variables to store tasks (starting as empty or with a default value)
task1 = None
task1Status = None
task2 = None
task2Status = None
task3 = None
task3Status = None
taskCounter = 0

# Create a loop to keep the menu active until the user chooses "exit".
# Allows repeating the addition of tasks.
print("===================================")
print(" Welcome to the Task Manager ")
print("===================================\n")

print("Choose an option:")
print("1 - View tasks")
print("2 - Add task")
print("3 - Exit")

# .strip() ensures that the user's input has no extra spaces before or after,
# making option verification easier.
option = input("Enter the number of the desired option: ").strip()

while option != "3":
    if option == "1":
        print("\n--- Your Tasks ---")
        # Check if there are tasks to display
        if task1:
            print("1.", task1)
        if task2:
            print("2.", task2)
        if task3:
            print("3.", task3)
        if not task1 and not task2 and not task3:
            print("No tasks added yet.")
        print("--------------------\n")

    elif option == "2":
        if taskCounter < 3:
            new_task = input("Enter the new task: ").strip()
            if taskCounter == 0:
                task1 = new_task
            elif taskCounter == 1:
                task2 = new_task
            elif taskCounter == 2:
                task3 = new_task
            taskCounter += 1
            print("Task added successfully!\n")
        else:
            print("\nYou have already added the maximum number of tasks (3). Remove one to add another.\n")

    else:
        print("\nInvalid option. Please try again.\n")

    print("===================================")
    print(" Welcome to the Task Manager ")
    print("===================================\n")

    print("Choose an option:")
    print("1 - View tasks")
    print("2 - Add task")
    print("3 - Exit")

    # .strip() ensures that the user's input has no extra spaces before or after,
    # making option verification easier.
    option = input("Enter the number of the desired option: ").strip()

print("\nExiting the program. See you soon!")