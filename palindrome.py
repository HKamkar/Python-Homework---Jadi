userInput = input().lower()

inverseInput =  userInput[::-1]
#print(inverseInput)
if userInput == inverseInput:
    print('palindrome')
else:
    print('not palindrome')