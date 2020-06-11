import numpy as np 

def cdToSuf(cd, n):  # 座標→平坦配列
    return cd[0]+cd[1]*n

def sufToCd(suf, n):  # 平坦配列→座標
    return (suf%n, suf // n)

class Dijkstra:
    INF = 10000
    END = 20000
    OBS = 20001

    #d = Dijkstra(20, (0, 0), (8, 9), 20, [(2, 2), (2, 3)])
    def __init__(self, n, start, goal, height, obst):
        self.n = n  # 縦横セル数
        self.start = start  # 始点
        self.goal = goal #終点
        self.height = height #高度の差
        self.obst = obst #障害物リスト

        self.size = n*n
        self.dist = [-1 for i in range(self.size)]  # 決定距離
        self.unSearch = [Dijkstra.INF for i in range(self.size)]  # 未定距離)未探索:INF,決定済み:END,障害:OBS
        self.parent = [-1 for i in range(self.size)]  # 親
        self.route = []
        self.routeHeight = []

        self.unSearch[cdToSuf(start,self.n)] = 0

        for p in self.obst: #障害物設定
            self.unSearch[cdToSuf(p,self.n)] = Dijkstra.OBS

    def _update(self, x, v, p):  # 距離更新
        if(self.unSearch[x] < Dijkstra.END):  # 探索済み除外
            newDist = self.dist[v]+p
            if(self.unSearch[x] > newDist):  # もっと距離が短くなるとき
                self.unSearch[x] = newDist
                self.parent[x] = v

    def _searchDist(self, v):  # 周囲の点を見る
        for i in [-1, 1]:
            x = v+i
            if(v//self.n == x//self.n):  # 横
                self._update(x, v, 1)
            x = v+i*self.n
            if(x >= 0 and x < self.size):  # 縦
                self._update(x, v, 1)
            for j in [-1, 1]:
                x = v+i*self.n+j
                if(x >= 0 and x < self.size and abs(v//self.n - x//self.n)==1):  # ナナメ
                    if(self.unSearch[v+i*self.n]!=Dijkstra.OBS and self.unSearch[v+j]!=Dijkstra.OBS):  # 障害除外
                        self._update(x, v, 1.5)

    def _searchRoute(self):
        place = cdToSuf(self.goal,self.n)
        nextP = self.parent[place]
        while(nextP!=-1):
            self.route.insert(0,sufToCd(place,self.n))
            place = nextP
            nextP = self.parent[place]
        self.route.insert(0,sufToCd(place,self.n))

    def _upHeight(self): #後ろから高度を加算
        for e in self.route:
            self.routeHeight.append([e[0],e[1],0])
        width = len(self.route) - 1
        i = width - 1
        j = self.height
        while(j>0):
            self.routeHeight[i+1][2]+=1
            i = (i-1)%width
            j -= 1

    def search(self):
        for i in range(self.size-len(self.obst)):
            # 距離が最小値の点を抽出
            v = self.unSearch.index(min(self.unSearch))
            self.dist[v] = self.unSearch[v]
            self.unSearch[v] = Dijkstra.END
            self._searchDist(v)
        self._searchRoute()
        self._upHeight()