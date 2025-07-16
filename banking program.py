#Banking Program
#from courses.ascii import isalpha


#import time

#def count(end, start=0):
    #for x in range(start, end+1):
      #  print(x)
#time.sleep(1)
#print('Done!')

#count(30, 25)

#def i_was_broken(greeting, name, emotion):
   # print(f'{greeting} {name} {emotion}')

#i_was_broken('heyy', emotion='broke me' , name='Crystal')
#print('1','2','3', sep='-')

#def add_numbers(**moneys):
   # for key, value in moneys.items():
       # print(f'{key}: {value}')

#list compression are short hands for simplicity in python.
#fruits = ['strawberry', 'blackberry', 'pineapple', 'watermelon']
#fruits = [fruit.replace('s', 'p') for fruit in fruits if fruit[0]=='s']
#print(fruits)

def show_balance(balance):
    print("************************")
    print(f'Your balance is ${balance:.2f}')
    print("************************")


def deposit():
        amount = float(input('Enter amount to deposit: '))
        if amount<0:
            print('Invalid Amount')
            return 0
        else:
            return amount

def withdraw(balance):
    amount =  float(input('Enter amount to withdraw: '))
    if amount < 0:
        print("Invalid amount")
        return 0
    elif amount > balance:
        print("Insufficient Balance")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print('***********************')
        print('****Banking Program****')
        print("1)Deposit")
        print("2)Withdraw")
        print("3)Check Balance")
        print("4)Exit")
        print('***********************')

        choice = input('Enter your choice(1-4): ')

        if choice == "1":
            balance += deposit()
            show_balance(balance)
        elif choice == "2":
            balance -= withdraw(balance)
            show_balance(balance)
        elif choice == "3":
            show_balance(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid Choice!")

    print("Thanks for visiting")

if __name__ == "__main__":
    main()


















