# start with the smallest possible number so it will be replaced by the first input
largest = float('-inf')  # begins with the lowest possible number

while True:
    number = input("Enter a number or type 'exit': ")

    # establish the word 'exit' as the stop signal (sentinel)
    if number.lower() == 'exit':
        break

    if float(number) > largest:
        largest = float(number)

print("Largest number:", largest)