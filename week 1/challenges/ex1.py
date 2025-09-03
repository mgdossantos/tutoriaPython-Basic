# Create a program that asks the user for their year of birth and calculates their current age.
# Then, display a message indicating whether the user is an adult or a minor.

name = input("Enter your name: ")
birth_year = int(input("Enter your year of birth: "))

current_age = 2025 - birth_year
status = "an adult" if current_age >= 18 else "a minor"

print(name, "you are", status + ".")