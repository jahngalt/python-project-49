import prompt
import random

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name 

def game_core(someName):
    score = 0
    while score < 3:
        i = random.randint(0, 100)
        print(f"Question: {i}")
        answer = str(input("Your answer: "))
        if i % 2 == 0 and answer.lower() == 'yes': 
            score += 1
            print('Correct!')
        elif i % 2 != 0 and answer.lower() == 'no':
            score += 1
            print('Correct!')
        else:
            print(f'\'yes\' is wrong answer ;(. Correct answer was \'no\'.\nLet\'s try again, {someName}!')
            break
    if score >= 3:
        print(f"Congratulations, {someName}!")
            