age1 = 0
age2 = 0
i = 0
while i != -1:
    i = int(input())
    if i > age1:
        age2 = age1
        age1 = i
    else:
        if i > age2:
            age2 = i
            
print(age1, age2)