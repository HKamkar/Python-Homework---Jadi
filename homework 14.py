#By Hossein Kamkar

nameList = ['']
name = ''
i = 0
while i < 10:
    name = input()
    name = name.lower()
    name = name.capitalize()
    nameList.append(name)
    i += 1
    
i = 1
while i < len(nameList):
    print(nameList[i])
    i += 1