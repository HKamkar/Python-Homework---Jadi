# By Hossein Kamkar
import random

a = 0
b = 99
while True:
    guess = random.randint(a,b)
    print(guess)
    userInput = input()
    
    if userInput == 'k':
        b = guess
        guess = random.randint(a,b-1)
    elif userInput == 'b':
        a = guess
        guess = random.randint(a+1,b)
    elif userInput == 'd':
        print('End')
        break
    