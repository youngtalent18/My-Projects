import random

lowest_num = 1
highest_num = 50
guesses = 0
is_running = True
answer = random.randint(lowest_num, highest_num)

print(f'Guess a the number between {lowest_num} and {highest_num}: ')

while is_running:
    guess = input('Enter your guess: ')
    if guess.isdigit():
        guess = int(guess)
        guesses+=1
        if guess < lowest_num and guess > highest_num:
            print('Your guess is out of range')
            print('Guess between 1-50')
        elif guess > answer:
            print('Too high, try again!')
        elif guess < answer:
            print('Too low , try again!')
        else:
            print('Correct!')
            print(f'The correct answer was {answer}, you nailed it. It took you {guesses} attempts')
            is_running = False
    else:
        print('Invalid Guess!')
        print(f'Please select a number between {lowest_num} and {highest_num}')


