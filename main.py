import numpy as np
import xlrd
from excelinput import *
from dijstra import *

path0 = r"path of dataset.xlsx"

Adjacent = excelinput(path0)
Adjacent = np.array(Adjacent)


Result = dijstra(Adjacent, 0, 1)
for N in range(15, 16):
    print("*when choose", N, "features")
    for Src in range(0, Adjacent.shape[1]):
        Adjacent = excelinput(path0)
        if dijstra(Adjacent, Src, N) > Result:
            Adjacent = excelinput(path0)
            Result = dijstra(Adjacent, Src, N)
        print( Src, "node")
    Adjacent = excelinput(path0)
    print(Result)
    print("***Best")


# Src, N = 0, 3
# dijstra(Adjacent, Src, N)
# Src denotes the number of the start point, Dst denotes the number of the end point and N denotes the number of nodes.
# dist is a list of distances from the starting point to each node（so the starting point is to be assigned the value0:dist[src] = 0），The function of the book is to record the list of nodes for which the shortest distance has been determined.


