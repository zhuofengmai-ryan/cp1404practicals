"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
BASIC_SALES = 0
UPPER_SALES = 1000
LOW_BONUS_RATE = 0.1
HIGH_BONUS_RATE = 0.15
sales = float(input("Enter sales: $"))
while sales >= BASIC_SALES:
    if sales < UPPER_SALES:
        bonus = sales * LOW_BONUS_RATE
    else:
        bonus = sales * HIGH_BONUS_RATE
    print(f"Bonus: ${int(bonus)}")
    sales = float(input("Enter sales: $"))
