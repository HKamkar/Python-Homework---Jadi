numberOfPlayer = int(input())
records = input()
recordsList = records.split()
recordsList.sort()

for i in range(0,numberOfPlayer):
    recordsList[i] = int(recordsList[i])
    if recordsList[i] > 2: 
        recordsList[i] = 'must delete'

while 'must delete' in recordsList:
    recordsList.remove('must delete')

numberOfTeam = int(len(recordsList) / 3)
print(numberOfTeam)