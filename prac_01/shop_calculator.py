DISCOUNT = 0.1
MINIMUM_PRICE = 0
DISCOUNT_REQUIRE = 100

number_of_items = int(input("Number of items: "))
total_price = 0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    while price < MINIMUM_PRICE:
        print("Invalid number of items!")
        price = float(input("Price of item: "))
    else:
        total_price += price

if total_price >= DISCOUNT_REQUIRE:
    total_price *= (1 - DISCOUNT)
print(f"Total price for {number_of_items} items is ${total_price:,.2f}")
