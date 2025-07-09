# -----Temperature Conversion Program-----

temp = float(input("Enter your temperature: "))
unit = input("Is this unit in celsius or fahrenheit(°C,°F,): ").upper()

if unit == 'C':
    temp =  round((9/5 * temp) + 32, 1)
    print(f'Your temperature in fahrenheit is {temp}°F')
elif unit == 'F':
    temp = round((temp - 32) * 5/9, 1)
    print(f'Your temperature in Celsius is {temp}°C')
else:
    print(f'{unit} is an invalid choice')

