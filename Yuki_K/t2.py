# -------- NOTE: Naming 'scipy.py' causes an error -------

import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import lil_matrix, csr_matrix, coo_matrix
from scipy import sparse
import sys

xSIZE = 100
ySIZE = 100
zSIZE = 100
N = xSIZE*ySIZE*zSIZE
start = 0  # NUM形式
end = 6  # NUM形式
obst = [[1, 0, 0], [2, 2, 1]]
data = []
row = []
col = []


def cd(n):  # 座標に直す
    return (n % xSIZE, n % (xSIZE*ySIZE)//xSIZE, n//(xSIZE*ySIZE))


def num(x, y, z):  # 番号に直す
    return x+y*xSIZE+z*(xSIZE*ySIZE)


def makeData(d, i, j):
    if d > 0:
        data.append(d)
        row.append(i)
        col.append(j)


def init():
    for i in range(N):
        if i % 10000 == 0:
            sys.stdout.write("\r処理中: "+str((int)(i/N*100))+"%")
            sys.stdout.flush()
        chkList = []
        location = cd(i)
        for a in range(-1, 2):
            for b in range(-1, 2):
                for c in range(-1, 2):
                    ap = i+a+b*xSIZE+c*(xSIZE*ySIZE)
                    if i < ap and ap < N:
                        check = cd(ap)
                        cnt = 0
                        for s in range(3):
                            dist = abs(location[s]-check[s])
                            if dist == 1:
                                cnt += 1
                            elif dist > 1:
                                cnt = 0
                                break
                        makeData(np.sqrt(cnt), i, ap)
        # print(chkList)
    return coo_matrix((data, (row, col)), (N, N)).tocsr()
# 障害物部分を0にする必要がある


def path(ar):
    #d, p = shortest_path(ar, indices=start, return_predecessors=True)
    d, p = shortest_path(ar, indices=start, directed=False,
                         return_predecessors=True)
    path = []
    i = end
    while i != start and i >= 0:
        path.append(i)
        i = p[i]
    if i < 0:
        return []
    path.append(i)
    # ☆return -> path[::-1]
    ans = path[::-1]
    for j in range(len(ans)):
        ans[j] = cd(ans[j])
    return ans


ar = init()

print("")

#print(ar)

print(path(ar))
