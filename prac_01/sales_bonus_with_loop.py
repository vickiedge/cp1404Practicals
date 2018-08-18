"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
Loop to continue above until sales is a negative.
"""
sales = float(input("Enter sales: $ "))
while sales > 0:
    if sales < 1000:
        bonus = sales * 10 / 100
    else:
        bonus = sales * 15 / 100
    print("Bonus: $ {:.2f}".format(bonus))
    sales = float(input("Enter sales: $ "))
print("No bonus")