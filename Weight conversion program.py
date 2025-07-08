#Weight Conversion Program

weight = float(input("Enter your weight: "))
unit = input("Enter your unit (kg or lbs): ")

if unit == 'kg':
    weight *= 2.025
    unit = 'lbs'
    print(f'Your weight is {round(weight,2)}{unit}')
elif unit == 'lbs':
    weight /= 2.025
    unit = 'kg'
    print(f'Your weight in kilogram is {round(weight,2)}{unit}')
else:
    print("Please enter the preferred unit")