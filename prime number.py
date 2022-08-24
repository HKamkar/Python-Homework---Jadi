number = input()
number = int(number)

checkPrime = 0
for i in range(2,number):
    if number % i == 0:
        checkPrime += 1

if checkPrime == 0:
    print('prime')
else:
    print('not prime')