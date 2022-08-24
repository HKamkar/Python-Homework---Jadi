#Written by Hossein Kamkar
import numpy as np

#exercise's matrix
a = np.array([[12.11,-7.9,9.23],
             [5.06,6.35,21.7],
             [-3.34,2.67,14.38]])

#exercise 1 question 1-3:
absoluteofA = np.absolute(a)
answer1 = np.log(absoluteofA)
answer2 = np.sqrt(absoluteofA)
answer3 = np.tanh(a)

#exercise 1 question 4: sum of each column
answer4 = np.sum(a,0)


#exercise 1 question 5: sort each row
sortedByRow = np.eye(3)
sortedByRow = np.sort(a)
answer5 = np.zeros((3,2))
answer5[:,0] = sortedByRow[:,0]
answer5[:,1] = sortedByRow[:,2]

#exercise 1 question 6: sum of main diagonal
sumOfDiagonal = np.sum(a.diagonal())

#exercise 1 question 7: sort each column
sortedByColumn = np.eye(3)
sortedByColumn = np.sort(a,0)

#Export answers in a classy way
print('Please type the question number, enter -1 to quite')
questionNumber = 0

while questionNumber != -1:
    questionNumber = int(input('from 1 to 7, -1 to quite: '))
    if questionNumber == 1:
        print('Ln|A|: ')
        print(answer1)
    elif questionNumber == 2:
        print('Square root of |A|:')
        print(answer2)
    elif questionNumber == 3:
        print('tanh of A:')
        print(answer3)
    elif questionNumber == 4:
        print('sum of each column:')
        print(answer4)
    elif questionNumber == 5:
        print('minimum and maximum of each row:')
        print(answer5)
    elif questionNumber == 6:
        print('sum Of main Diagonal:')
        print(sumOfDiagonal)
    elif questionNumber == 7:
        print('sorted A (by column): ')
        print(sortedByColumn)
    elif questionNumber == -1:
        print('Quiting...')
    else:
        print('From 1 to 7, or -1 to quite ok?')