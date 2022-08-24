#Written by Hossein Kamkar

from pkg_resources import yield_lines


inputString = input()
myList = inputString.split()
for i in range(0,len(myList)):
    myList[i] = float(myList[i])
myList.sort()

length = myList[-1] - myList[0]
if length % 1 == 0:
    print(int(length))
else:
    print(length)
