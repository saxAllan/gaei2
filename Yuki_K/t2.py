import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

xSIZE = int(input("xSIZE:"))
ySIZE = int(input("ySIZE:"))
zSIZE = int(input("zSIZE:"))
N = xSIZE*ySIZE*zSIZE
start = 0  # NUM形式
end = 3  # NUM形式


def cd(n):  # 座標に直す
    return (n % xSIZE, n % (xSIZE*ySIZE)//xSIZE, n//(xSIZE*ySIZE))


def num(x, y, z):  # 番号に直す
    return x+y*xSIZE+z*(xSIZE*ySIZE)


def init():
    ar = np.zeros((N, N))
    for i in range(N):
        chkList = [i-1, i+1, i-xSIZE, i+xSIZE,
                   i-(xSIZE*ySIZE), i+(xSIZE*ySIZE)]
        location = cd(i)
        print(i, chkList, end="")
        for e in chkList:
            check = cd(e)
            if check[2] < 0 or N <= check[2]:
                continue
            print(e, end="")
            cnt = 0
            for s in range(3):
                if abs(location[s]-check[s]) == 1:
                    cnt += 1
            ar[i][e] = np.sqrt(cnt)
        print("")
    return ar
# 障害物部分を0にする必要がある
# 隣接セルのみ1にする処理


ar = init()

print(ar)

d, p = shortest_path(ar, indices=start, return_predecessors=True)

# print(p)


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


#print(get_path_row(start, end, p))
