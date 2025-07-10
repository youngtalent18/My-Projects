#ROCK---PAPER---SCISSORS---GAME

import random

options = ('Rock', 'Paper', 'Scissors')
running = True
player = None
computer = random.choice(options)

while running:
    player = None
    computer = random.choice(options)
    while player not in options:
        player = input('Enter a choice (Rock, Paper, Scissors): ')

        print(f'Player: {player}')
        print(f'Computer: {computer}')

        if player == computer:
            print('It is a tie')
        elif player == 'Rock' and computer == 'Scissors':
            print('You win!')
        elif player == 'Paper' and computer == 'Rock':
            print('You win!')
        elif player == 'Scissors' and computer == 'Paper':
            print('You win!')
        else:
            print('You lose')

        play_again = input('Want to play again?(y/n): ').lower()
        if not play_again == 'y':
            running = False