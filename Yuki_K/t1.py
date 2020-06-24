import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

l = [[0, 1, 2, 0],
     [0, 0, 0, 1],
     [3, 0, 0, 3],
     [0, 0, 0, 0]]

# print(shortest_path(l))
# AttributeError: 'list' object has no attribute 'shape'

a = np.array(l)
print(type(a))
# <class 'numpy.ndarray'>

print(shortest_path(a))
# [[ 0.  1.  2.  2.]
#  [inf  0. inf  1.]
#  [ 3.  4.  0.  3.]
#  [inf inf inf  0.]]

print(type(shortest_path(a)))
# <class 'numpy.ndarray'>

csr = csr_matrix(l)
print(csr)
#   (0, 1)  1
#   (0, 2)  2
#   (1, 3)  1
#   (2, 0)  3
#   (2, 3)  3

print(type(csr))
# <class 'scipy.sparse.csr.csr_matrix'>

print(shortest_path(csr))
# [[ 0.  1.  2.  2.]
#  [inf  0. inf  1.]
#  [ 3.  4.  0.  3.]
#  [inf inf inf  0.]]

print(shortest_path(csr, indices=0))
# [0. 1. 2. 2.]

print(shortest_path(csr, indices=[0, 3]))
# [[ 0.  1.  2.  2.]
#  [inf inf inf  0.]]

print(shortest_path(csr, directed=False))
# [[0. 1. 2. 2.]
#  [1. 0. 3. 1.]
#  [2. 3. 0. 3.]
#  [2. 1. 3. 0.]]

l_ud = [[0, 1, 2, 0],
        [1, 0, 0, 1],
        [2, 0, 0, 3],
        [0, 1, 3, 0]]

print(shortest_path(csr_matrix(l_ud)))
# [[0. 1. 2. 2.]
#  [1. 0. 3. 1.]
#  [2. 3. 0. 3.]
#  [2. 1. 3. 0.]]

d, p = shortest_path(csr, return_predecessors=True)

print(d)
# [[ 0.  1.  2.  2.]
#  [inf  0. inf  1.]
#  [ 3.  4.  0.  3.]
#  [inf inf inf  0.]]

print(p)
# [[-9999     0     0     1]
#  [-9999 -9999 -9999     1]
#  [    2     0 -9999     2]
#  [-9999 -9999 -9999 -9999]]

def get_path(start, goal, pred):
    return get_path_row(start, goal, pred[start])

def get_path_row(start, goal, pred_row):
    path = []
    i = goal
    while i != start and i >= 0:
        path.append(i)
        i = pred_row[i]
    if i < 0:
        return []
    path.append(i)
    return path[::-1]

print(get_path(0, 3, p))
# [0, 1, 3]

print(get_path(2, 1, p))
# [2, 0, 1]

print(get_path(3, 3, p))
# [3]

print(get_path(3, 1, p))
# []

d2, p2 = shortest_path(csr, indices=2, return_predecessors=True)

print(d2)
# [3. 4. 0. 3.]

print(p2)
# [    2     0 -9999     2]

print(get_path_row(2, 1, p2))
# [2, 0, 1]

print(get_path_row(2, 0, p2))
# [2, 0]