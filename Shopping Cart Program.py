#Shopping Cart Program

cart = []

prices = []
total = 0

while True:
    food = input('Enter foods or q to quit: ').lower()
    if food == 'q':
        break
    else:
        price = int(input(f'Enter the price of {food}: '))
        cart.append(food)
        prices.append(price)

print('------Your Cart-----')

for food in cart:
    print(food, end=' ')

for price in prices:
    total += price

print()
print(f'Your total cost is ${total}')