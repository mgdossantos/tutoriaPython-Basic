# Create a mini shopping simulator: the program should ask for the price of two products
# and display the total amount and the 10% discount applied.

product1 = float(input("Enter the price of product 1: "))
product2 = float(input("Enter the price of product 2: "))

total = product1 + product2
discount = 0.1 * total

print("Total: $", total)
print("Discount to be applied: $", discount)