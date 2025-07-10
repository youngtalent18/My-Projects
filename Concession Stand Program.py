# Concession stand program

menu = {
    'burger':3.00,
    'pizza':2.50,
    'rice':5.00,
    'sushi':3.20,
    'coke':6.00,
    'hamburger':4.50,
    'cocktail': 6.00
}

cart = []
total = 0

while True:
    food = input('Enter the food to place order or q to quit: ').lower()
    if food == 'q':
        break
    elif menu.get(food) != None:
        cart.append(food)

print('-----🛒Your Order🛒-----')
for food in cart:
    total += menu.get(food)
    print(food)

print()
print(f'Your total cost is : ${total:.2f}')