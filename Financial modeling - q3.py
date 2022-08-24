#Written by Hossein Kamkar
import numpy as np

matrixB = np.zeros((3,7))
matrixB[0] = np.arange(1,8)
matrixB[1] = np.arange(9,-4,-2)
matrixB[2] = np.geomspace(4,256,7)
print(matrixB)