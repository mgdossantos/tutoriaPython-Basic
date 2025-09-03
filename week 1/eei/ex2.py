# Ask the user for an integer number and display whether it is even or odd
# (use mathematical and relational operators).

number = int(input("Enter a number to test: "))

# Conditional expression to check even or odd
result = "Even" if number % 2 == 0 else "Odd"
print("The number", number, "is", result)