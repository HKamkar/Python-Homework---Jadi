import numpy as np

oneMatrix1 = np.ones((3,5))
desiredMatrix1 = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]

oneMatrix2 = np.ones((5,3))
desiredMatrix2 = [[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4]]

print(np.multiply(oneMatrix1,desiredMatrix1))
print(np.multiply(oneMatrix2,desiredMatrix2))