#shopping cart

food = []
price = []
total = 0

while True:
    item = input("Enter the item: ")
    if item.lower() == "q":
        break
    else:
        prices = float(input("Enter the price of the {food}: "))
        food.append(foods)
        price.append(prices)

print(----------YOUR CART--------)
print()

for foods in food:
    print(foods)

for prices in price:    
    total += prices

print(f'Total Prices: {total:.2f} $')
