import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import lil_matrix, csr_matrix, coo_matrix
from scipy import io, sparse
import sys


class SciSearch:
    def _cd(self, n):  # 座標に直す
        return (n % self.xSIZE, n % (self.xSIZE*self.ySIZE)//self.xSIZE, n//(self.xSIZE*self.ySIZE))

    def _num(self, x, y, z):  # 番号に直す
        return x+y*self.xSIZE+z*(self.xSIZE*self.ySIZE)

    def _setObst(self):
        lil = self.csr.tolil()
        for o in self.obst:
            for i in range(o[2]+1):  # obst入力方法更新！(7/9更新)
                obstNum = self._num(o[0], o[1], i)
                lil[:, obstNum] = 0
                lil[obstNum, :] = 0
        self.csr = lil.tocsr()  # スライスができる！！！！！(7/9更新)

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

        if mode == 1:  # １から生成＋ファイル書き込み（mode=1)(7/9更新)
            self._createData()
            self.csr = csr_matrix(
                (self.data, (self.row, self.col)), (self.N, self.N))
            io.savemat("mat_" +
                       str(self.xSIZE) + "_" + str(self.ySIZE) +
                       "_" + str(self.zSIZE) + ".mat", {"CSR": self.csr})
        elif mode == 2:  # ファイルから読み込み（mode=2)(7/9更新)
            self.csr = io.loadmat("mat_" +
                                  str(self.xSIZE) + "_" + str(self.ySIZE) +
                                  "_" + str(self.zSIZE) + ".mat")["CSR"]
        self._setObst()

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
