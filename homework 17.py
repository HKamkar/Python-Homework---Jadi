userInput = input().upper()
if userInput.find('AB') != -1:
    userInput = userInput.replace('AB','CC') #this line replace all AB strings, not just one
    #print(userInput)
    if userInput.find('BA') != -1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')