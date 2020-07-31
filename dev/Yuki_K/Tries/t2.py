# -------- NOTE: Naming 'scipy.py' causes an error -------

import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import lil_matrix, csr_matrix, coo_matrix
from scipy import sparse
import sys

xSIZE = 100
ySIZE = 100
zSIZE = 20
N = xSIZE*ySIZE*zSIZE
start = 0  # NUM形式
end = 6  # NUM形式
obst = [[[1, 0, 0], [2, 2, 1]], [[5, 1, 0], [7, 4, 0]]]
data = []
row = []
col = []


def cd(n):  # 座標に直す
    return (n % xSIZE, n % (xSIZE*ySIZE)//xSIZE, n//(xSIZE*ySIZE))


def num(x, y, z):  # 番号に直す
    return x+y*xSIZE+z*(xSIZE*ySIZE)


def appendData(d, i, j):
    if d > 0:
        data.append(d)
        row.append(i)
        col.append(j)


def writeList():
    l = [data, row, col]
    rwIndex = ["data", "row", "col"]
    for i in range(3):
        path = rwIndex[i] + "_" + \
            str(xSIZE) + "_" + str(ySIZE) + "_" + str(zSIZE) + ".dat"
        s = ""
        for e in l[i]:
            s += str(e)+" "
        with open(path, mode='w') as f:
            f.write(s)


def readData():
    rwIndex = ["data", "row", "col"]
    for i in range(3):
        path = rwIndex[i] + "_" + \
            str(xSIZE) + "_" + str(ySIZE) + "_" + str(zSIZE) + ".dat"
        with open(path) as f:
            s = f.read().split()
        if i == 0:
            for i in range(len(s)):
                data.append(float(s[i]))
        elif i == 1:
            for i in range(len(s)):
                row.append(int(s[i]))
        elif i == 2:
            for i in range(len(s)):
                col.append(int(s[i]))


def createData():
    for i in range(N):
        if i % 10000 == 0:
            sys.stdout.write("\rデータ生成中: "+str((int)(i/N*100))+"%")
            sys.stdout.flush()
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
                        appendData(np.sqrt(cnt), i, ap)
    sys.stdout.write("\r生成完了: 100%             \n")
    sys.stdout.flush()


def setObst():
    for obstRange in obst:
        rStart = obstRange[0]
        rEnd = obstRange[1]
        for i in range(rStart[0], rEnd[0]+1):
            for j in range(rStart[1], rEnd[1]+1):
                for k in range(rStart[2], rEnd[2]+1):
                    if (i+j+k)%3==0:
                        sys.stdout.write("\r障害物設定中.  ")
                    elif (i+j+k)%3==1:
                        sys.stdout.write("\r障害物設定中 . ")
                    elif (i+j+k)%3==2:
                        sys.stdout.write("\r障害物設定中  .")
                    sys.stdout.flush()
                    obstNum = num(i, j, k)
                    cnt = 0
                    while cnt < len(data):
                        if(col[cnt] == obstNum or row[cnt] == obstNum):
                            del col[cnt]
                            del row[cnt]
                            del data[cnt]
                        else:
                            cnt += 1
    sys.stdout.write("\r障害物設定完了    \n")
    sys.stdout.flush()


def init(mode):
    if mode == 1:  # １から生成（mode=1)
        createData()
    elif mode == 2:  # １から生成＋ファイル書き込み（mode=2)
        createData()
        writeList()
    elif mode == 3:  # ファイルから読み込み（mode=3)
        readData()
        print("読み込み完了")
    setObst()
    return csr_matrix((data, (row, col)), (N, N))



def searchPath(csr):  # Scipy経路探索
    d, p = shortest_path(csr, indices=start, directed=False,
                         return_predecessors=True)
    path = []
    i = end
    while i != start and i >= 0:
        path.append(i)
        i = p[i]
    if i < 0:
        return []
    path.append(i)
    ans = path[::-1]
    for j in range(len(ans)):
        ans[j] = cd(ans[j])
    return ans


csr = init(1)

print(searchPath(csr))
