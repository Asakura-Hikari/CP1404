"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))  # get variable for sales from terminal
bonus = ""  # create a variable for bonus

if 0 < sales < 1000:
    bonus = sales * 0.1
elif sales >= 1000:
    bonus = sales * 0.15
else:
    print("sales is Invalid")

print("$", sales, "'s bonus is", bonus)
