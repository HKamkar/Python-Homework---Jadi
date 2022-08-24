import numpy as np

matrixA = np.array([[2,9,0,0],
                    [0,4,1,4],
                    [7,5,5,1],
                    [7,8,7,4]])

matrixB = np.array([-1,6,0,9])

#Question 1
matrixC = np.eye(4,2)
matrixC[:,0] = matrixA[:,1]
matrixC[:,1] = matrixA[:,2]

#Question 2
matrixD = matrixA[0:2,1:3]


#Question 3
matrixX = np.zeros((4,1))
inverseOfA = np.linalg.inv(matrixA)
# Debug: When we multiply a matrix by its inverse we get the Identity Matrix (which is like "1" for matrices)
#matrixX = np.dot(matrixA, inverseOfA)
#print(matrixX)
matrixX = np.dot(inverseOfA,matrixB)
print(matrixX)