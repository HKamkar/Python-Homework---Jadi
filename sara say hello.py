#By Hossein Kamkar

from itertools import count


saraInput = input()
#saraInput = 'ahhelououlllloou'
countH = int(saraInput.find('h'))
inputSlice = saraInput[countH+1:]
#print(inputSlice)

countE = int(inputSlice.find('e')) + countH + 1
inputSlice = saraInput[countE+1:]
#print(inputSlice)

countL = int(inputSlice.find('l')) + countE + 1
inputSlice = saraInput[countL+1:]
#print(inputSlice)

count2ndL = int(inputSlice.find('l')) + countL + 1
inputSlice = saraInput[count2ndL+1:]
#print(inputSlice)

countO = int(inputSlice.find('o')) + count2ndL + 1

if countE > countH and countL > countE and count2ndL > countL and countO > count2ndL:
    print('YES')
else:
    print('NO')
    

print(countH)
print(countE)
print(countL)
print(count2ndL)
print(countO)
