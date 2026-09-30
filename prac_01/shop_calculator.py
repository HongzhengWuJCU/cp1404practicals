number_of_item=int(input("Number of item: "))
while number_of_item<0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of item again: "))
total_price=0
for i in range(number_of_item):
    price_of_item=float(input("Price_of_item:"))
    total_price+=price_of_item
if total_price >100:
    DISCOUNT_RATE=0.9
    total_price*=DISCOUNT_RATE
print(f"Total price for {number_of_item} items is ${total_price:.2f}")