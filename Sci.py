import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import lil_matrix, csr_matrix, coo_matrix
from scipy import sparse
import sys


class SciSearch:
    def _cd(self, n):  # 座標に直す
        return (n % self.xSIZE, n % (self.xSIZE*self.ySIZE)//self.xSIZE, n//(self.xSIZE*self.ySIZE))

    def _num(self, x, y, z):  # 番号に直す
        return x+y*self.xSIZE+z*(self.xSIZE*self.ySIZE)

    def _setObst(self):
        status = 0
        for obstRange in self.obst:
            print("\r障害物設定中... ", status, "/", len(self.obst), end="")
            status += 1
            sys.stdout.flush()
            rStart = obstRange[0]
            rEnd = obstRange[1]
            for i in range(rStart[0], rEnd[0] + 1):
                for j in range(rStart[1], rEnd[1]+1):
                    for k in range(rStart[2], rEnd[2] + 1):
                        '''
                        if (i+j+k) % 3 == 0:
                            sys.stdout.write("\r障害物設定中.  ")
                        elif (i+j+k) % 3 == 1:
                            sys.stdout.write("\r障害物設定中 . ")
                        elif (i+j+k) % 3 == 2:
                            sys.stdout.write("\r障害物設定中  .")
                        sys.stdout.flush()
                        '''
                        obstNum = self._num(i, j, k)
                        cnt = 0
                        while cnt < len(self.data):
                            if(self.col[cnt] == obstNum or self.row[cnt] == obstNum):
                                del self.col[cnt]
                                del self.row[cnt]
                                del self.data[cnt]
                            else:
                                cnt += 1

        sys.stdout.write("\r障害物設定完了    \n")
        sys.stdout.flush()

    def _readData(self):
        rwIndex = ["data", "row", "col"]
        for i in range(3):
            path = rwIndex[i] + "_" + \
                str(self.xSIZE) + "_" + str(self.ySIZE) + \
                "_" + str(self.zSIZE) + ".dat"
            with open(path) as f:
                s = f.read().split()
            if i == 0:
                for i in range(len(s)):
                    self.data.append(float(s[i]))
            elif i == 1:
                for i in range(len(s)):
                    self.row.append(int(s[i]))
            elif i == 2:
                for i in range(len(s)):
                    self.col.append(int(s[i]))

    def _writeList(self):
        l = [self.data, self.row, self.col]
        rwIndex = ["data", "row", "col"]
        for i in range(3):
            path = rwIndex[i] + "_" + \
                str(self.xSIZE) + "_" + str(self.ySIZE) + \
                "_" + str(self.zSIZE) + ".dat"
            s = ""
            for e in l[i]:
                s += str(e)+" "
            with open(path, mode='w') as f:
                f.write(s)

    def _appendData(self, d, i, j):
        if d > 0:
            self.data.append(d)
            self.row.append(i)
            self.col.append(j)

    def _createData(self):
        for i in range(self.N):
            if i % 10000 == 0:
                sys.stdout.write("\rデータ生成中: "+str((int)(i/self.N*100))+"%")
                sys.stdout.flush()
            location = self._cd(i)
            for a in range(-1, 2):
                for b in range(-1, 2):
                    for c in range(-1, 2):
                        ap = i+a+b*self.xSIZE+c*(self.xSIZE*self.ySIZE)
                        if i < ap and ap < self.N:
                            check = self._cd(ap)
                            cnt = 0
                            for s in range(3):
                                dist = abs(location[s]-check[s])
                                if dist == 1:
                                    cnt += 1
                                elif dist > 1:
                                    cnt = 0
                                    break
                            self._appendData(np.sqrt(cnt), i, ap)
        sys.stdout.write("\r生成完了: 100%             \n")
        sys.stdout.flush()

    def __init__(self, cd, start, end, obst, mode):
        self.xSIZE = cd[0]
        self.ySIZE = cd[1]
        self.zSIZE = cd[2]
        self.N = self.xSIZE*self.ySIZE*self.zSIZE
        self.start = self._num(start[0], start[1], start[2])
        self.end = self._num(end[0], end[1], end[2])
        self.obst = obst

        self.data = []
        self.row = []
        self.col = []

        if mode == 1:  # １から生成（mode=1)
            self._createData()
        elif mode == 2:  # １から生成＋ファイル書き込み（mode=2)
            self._createData()
            self._writeList()
        elif mode == 3:  # ファイルから読み込み（mode=3)
            self._readData()
            print("読み込み完了")
        self._setObst()
        self.csr = csr_matrix(
            (self.data, (self.row, self.col)), (self.N, self.N))

    def search(self):  # Scipy経路探索
        d, p = shortest_path(self.csr, indices=self.start, directed=False,
                             return_predecessors=True)
        path = []
        i = self.end
        while i != self.start and i >= 0:
            path.append(i)
            i = p[i]
        if i < 0:
            return []
        path.append(i)
        ans = path[::-1]
        for j in range(len(ans)):
            ans[j] = self._cd(ans[j])
        return ans
