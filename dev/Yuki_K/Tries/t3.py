import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import lil_matrix, csr_matrix, coo_matrix
from scipy import sparse

size = int(input("size: "))
N = size*size*size
print(N)

data = []
row = []
col = []

def makeData(d, i, j):
    if j<N:
        data.append(d)
        row.append(i)
        col.append(j)

print("---1---")
for i in range(N):
    if i % size != size-1:
        makeData(1, i, i+1)
    if i % (size*size) != (size-1)*size:
        makeData(1, i, i+size)
    makeData(1, i, i+size*size)
#print(row)
#print(col)
print(len(row))

#(data, (row, column))
coo = coo_matrix((data, (row, col)), (N, N))

print(coo)
