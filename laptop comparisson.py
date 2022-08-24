laptopNumber = int(input())
laptopProp = []
eachLaptop = []
# Getting Data
for i in range(0,laptopNumber):
    laptopProp.append(input())

#cleaning Data for comparission
for i in range(0,laptopNumber):
    eachLaptop.append(laptopProp[i].split(' '))
    
print(eachLaptop)

#Comparission
for i in range(0,laptopNumber):
    for j in range(0,laptopNumber):
        if eachLaptop[i-1][1] > eachLaptop[i][1]:
            print('happy irsa')
        else:
            print('poor irsa')