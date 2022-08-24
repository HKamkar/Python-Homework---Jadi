userInput = input()
upperCount = 0
lowerCount = 0
for i in userInput:
    if i.isupper() == True:
        upperCount = upperCount + 1
    elif i.islower() == True:
        lowerCount = lowerCount + 1
    #print(i)

if lowerCount < upperCount:
    userInput = userInput.upper()
else:
    userInput = userInput.lower()
    
print(userInput)