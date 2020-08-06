num = int(input("Number of items: "))
total = 0.0
while num <= 0:
    print("Invalid number, please enter again")
    number = int(input("Number of items: "))

for i in range(num):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9

print("Total price for", num, "items is $", total)


