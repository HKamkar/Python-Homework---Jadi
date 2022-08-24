def divisorNumber(x):
    count = 0
    for i in range(1,x+1):
        if x % i == 0:
            count += 1
            
    return(count)

adad = 0
adadDivisor = 0   
for i in range(1,21):
    number = int(input())
    numberDivisor = divisorNumber(number)
    adadDivisor = divisorNumber(adad)
    
    if numberDivisor > adadDivisor:
        adad = number
    elif numberDivisor == adadDivisor:
        if number > adad:
            adad = number
        
print(adad, adadDivisor)