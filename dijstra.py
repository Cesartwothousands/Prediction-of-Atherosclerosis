import numpy as np

def dijstra(Adj, src, n):
    adj = Adj
    Inf = -1
    dist = [Inf]* n
    dist[0] = 0
    turn = [src] * n

    # record the identified node
    # find the shortest route from the starting point to that point each time
    # total length
    for i1 in range(n-1):# Try n-1 times,
        adj[src][src] = Inf
        max = adj[src][0]
        turn[i1 + 1] = 0  # Choose one node
        for i2 in range(adj.shape[1]):  # Which Column
            if adj[src][i2] > max:
                max = adj[src][i2]
                turn[i1 + 1] = i2

        dist[i1 + 1] = max
        adj[:,src] = Inf
        src = turn[i1 + 1]
    Dist = np.sum(dist)

    print(" The longest path order is：",turn,'\n',"The longest path length is：",dist,'\n',"The total path length is：",Dist)
    return Dist