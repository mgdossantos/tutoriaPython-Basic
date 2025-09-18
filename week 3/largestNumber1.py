

number = input("Enter a number or type 'exit': ")

# establish the word 'exit' as the stop signal (sentinel)
# start with the smallest possible number so it will be replaced by the first input
largest = 0# begins with the lowest possible number

while number.lower() != 'exit':

    if float(number) > largest:
        largest = float(number)

    number = input("Enter a number or type 'exit': ")

print("Largest number:", largest)