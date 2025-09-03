# Ask the user to enter two numeric variables and display:
# Sum, subtraction, multiplication, and division
# Greater than, less than, equal to, and different from
# Perform the operations of the first number with the second

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Arithmetic operations
sum_result = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2

print("Sum:", sum_result)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# Relational operations (comparisons)
greater = number1 > number2
print("Is the first number greater than the second?", greater)

less = number1 < number2
print("Is the first number less than the second?", less)

equal = number1 == number2
print("Is the first number equal to the second?", equal)

different = number1 != number2
print("Is the first number different from the second?", different)