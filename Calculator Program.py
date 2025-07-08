# My Calculator Program

operator = input("Enter an operator(+ - / *): ") #Asking user for an operator choice
num1 = float(input('Enter number 1: ')) #Ask user for number 1
num2 = float(input('Enter number 2: ')) #Asks user for the 2nd number

if operator == '+':
    result = num1 + num2
    print(round(result,2))
elif operator == '-':
    result = num1 - num2
    print(round(result, 2))
elif operator == '/':
    result = num1/num2
    print(round(result,2))
elif operator == '*':
    result = num1*num2
    print(round(result,2))
else:
    print('Invalid Operator Choice!')

