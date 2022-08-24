from operator import itemgetter
from typing import OrderedDict


def checkPrime(number):
    checkPrime = 0
    for i in range(2,number):
        if number % i == 0:
            checkPrime += 1

    if checkPrime == 0:
        return(1)
    else:
        return(0)


def divisorNumber(x):
    count = 0
    for i in range(2,x):
        if x % i == 0:
            if checkPrime(i):
                count += 1
            
    return(count)
                    

user_input = []
sorted_divisor_count = OrderedDict()

for i in range(10):
    user_input.append(int(input()))
    
for n in user_input:
    sorted_divisor_count.update({n: divisorNumber(n)})

sorted_divisor_count = sorted(sorted_divisor_count.items(), key=itemgetter(1), reverse= True)

for n in sorted_divisor_count[n][1]:
    print(n)

print(sorted_divisor_count)
    
