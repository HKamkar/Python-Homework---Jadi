#Written by Hossein Kamkar
from math import sqrt
from math import floor
#print float with n decimals without rounding
def truncate(f, n):
    return floor(f * 10 ** n) / 10 ** n

input_number = int(input())
numbers = []
square_root = []

for i in range(0,input_number):
    numbers.append(int(input()))
    
for i in range(0,input_number):  
    square_root.append(truncate(sqrt(numbers[i]),4))
    print("%.4f" % square_root[i])

