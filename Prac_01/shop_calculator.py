# allows the user to enter a number of items and the price of each
# compute and display the total price of those items
# if total price is over $100, then a 10% discount is applied before the total amount is displayed


total_price = 0
number = int(input("Price: $"))
while number < 0:
    print("invalid number of items")
    number = int(input("number of items:"))
for i in range(number):
    price = float(input("Price of item:"))
    total_price += price

if total_price > 100:
    total_price *= 0.9  # apply discount

print("Total price for", number, "items is $", total_price, sep='')

print("total price for {} items is ${:.2f}".format(number, total_price))
