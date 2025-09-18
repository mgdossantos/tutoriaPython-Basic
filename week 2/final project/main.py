# Creation of the initial skeleton for the task manager (Python file, general structure).
# Simple terminal interface: first welcome message in the program.

print("===================================")
print(" Welcome to the Task Manager ")
print("===================================\n")

print("Choose an option:")
print("1 - View tasks")
print("2 - Add task")
print("3 - Exit")

# .strip() ensures that the user's input has no extra spaces before or after,
# making option checking easier.
option = input("Enter the number of the desired option: ").strip()

if option == "1":
    print("\n[View tasks functionality not implemented yet]\n")
elif option == "2":
    print("\n[Add task functionality not implemented yet]\n")
elif option == "3":
    print("\nExiting the program. See you soon!")
else:
    print("\nInvalid option. Please try again.\n")

