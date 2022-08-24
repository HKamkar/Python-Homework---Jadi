#Wtitten by Hossein Kamkar

numberOfWords = int(input())
dictionary = dict()

#Creating custom dict
for i in range(0, numberOfWords):
    userInput = input()
    userInput = userInput.split(' ')
    #print(userInput) #debug
    dictionary.update({userInput[0]:userInput[1]})

#get and analyse the user sentence    
userSentence = input()
userSentence = userSentence.split(' ')
#print(userSentence)

#replace translation
for i in userSentence:
    if i in dictionary:
        userSentence[userSentence.index(i)] = dictionary.get(i)
        

print(' '.join(userSentence))