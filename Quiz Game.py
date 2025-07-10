# My Quiz Game.
#using tuples because it's ordered and faster
questions = ("1)Take the odd one out!", "2)How many bones are there in the human body?", "3)Which organ in the human body is responsible for pumping blood: ", "4)Which device is used to measure the speed of the wind? ")

options = (('A)Vein', 'B)Brain', 'C)Artery', 'D)Capillaries'),
           ('A)203', 'B)206', 'C)205', 'D)200'),
           ('A)Heart', 'B)Muscle', 'C)Liver', 'D)Pump'),
           ('A)Hydraulic Pressure', 'B)Barometer', 'C)Wind Vane', 'D)Anemometer'))

answers = ('B','B','A','D') #answer keys
score = 0 #initial score of the player
guesses = [] #store the total guesses

question_number = 0 #initial question before

print('*****Quiz ❤ Game****') #for decoration
for question in questions: # for each question in questions
    print(question) #it returns each question on a new line
    print('*********************') #for decoration
    for option in options[question_number]:# for each option in option
        print(option) #It returns each option

    guess = input('Enter your answer: ').upper() #Asks user for anwswer after every question
    guesses.append(guess) #embeds the users guess into the guesses list.
    if guess == answers[question_number]: #checks if answer is right
        print('Correct!')
        score +=1 #There's an increase in score after every successful correct
    else:
         print('Incorrect!')
         print(f'The correct answer is {answers[question_number]}')#shows the right answer

    question_number += 1 #Increase question

print('********************************')#for decoration
print('**********  RESULTS  ***********')#for decoration
print('********************************')#for decoration

print('Guesses: ', end=" ")
for guess in guesses: #return a sequence of the player's guess
    print(guess, end=" ")

print()

print('Answer: ', end=" ")
for answer in answers: #return a sequence of the right answer
    print(answer, end=" ")

print()

score = int((score/len(questions))*100) #calculates the total score after the game
print(f'Your score is {score}%')