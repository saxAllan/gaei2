import numpy as np
import draw
INF = 10000
END = 20000
OBS = 20001

#関数化

n = 20  # 縦横セル数
start = (0, 0)  # 始点
goal = (8,9)
height = 20
obst = [(2, 2), (2, 3)]

size = n*n
dist = [-1 for i in range(size)]  # 決定距離
unSearch = [INF for i in range(size)]  # 未定距離)未探索:INF,決定済み:END,障害:OBS
parent = [-1 for i in range(size)]  # 親
route = []
routeHeight = []


def cdToSuf(cd):  # 座標→平坦配列
    return cd[0]+cd[1]*n


def sufToCd(suf):  # 平坦配列→座標
    return (suf%n, suf // n)


def setObst(cd):  # 障害物設定
    unSearch[cdToSuf(cd)] = OBS


unSearch[cdToSuf(start)] = 0

for t in obst:
    setObst(t)


def update(x, v, p):  # 距離更新
    if(unSearch[x] < END):  # 探索済み除外
        newDist = dist[v]+p
        if(unSearch[x] > newDist):  # もっと距離が短くなるとき
            unSearch[x] = newDist
            parent[x] = v


def searchDist(v):  # 周囲の点を見る
    for i in [-1, 1]:
        x = v+i
        if(v//n == x//n):  # 横
            update(x, v, 1)
        x = v+i*n
        if(x >= 0 and x < size):  # 縦
            update(x, v, 1)
        for j in [-1, 1]:
            x = v+i*n+j
            if(x >= 0 and x < size and abs(v//n - x//n)==1):  # ナナメ
                if(unSearch[v+i*n]!=OBS and unSearch[v+j]!=OBS):  # 障害除外
                    update(x, v, 1.5)

def searchRoute():
    place = cdToSuf(goal)
    nextP = parent[place]
    while(nextP!=-1):
        route.insert(0,sufToCd(place))
        place = nextP
        nextP = parent[place]
    route.insert(0,sufToCd(place))

def upHeight(): #後ろから高度を加算
    for e in route:
        routeHeight.append([e[0],e[1],0])
    width = len(route) - 1
    i = width - 1
    j = height
    while(j>0):
        routeHeight[i+1][2]+=1
        i = (i-1)%width
        j -= 1

for i in range(size-len(obst)):
    # 距離が最小値の点を抽出
    v = unSearch.index(min(unSearch))
    dist[v] = unSearch[v]
    unSearch[v] = END
    searchDist(v)

searchRoute()
upHeight()
print(routeHeight)

d1 = draw.Draw(30, n)
for i in range(size):
    if(unSearch[i]==20001):
        d1.drawObst(sufToCd(i), (192,192,192))

for i in range(size):
    if(parent[i] != -1):
        d1.drawLine(sufToCd(i), sufToCd(parent[i]), (0,0,255))

for i in range(size):
    if(unSearch[i]==20001):
        col=(128,128,128)
    else:
        col=(0,128,0)
        d1.drawChara(sufToCd(i),str(dist[i]))
    d1.drawRect(sufToCd(i), col)

d1.show()
