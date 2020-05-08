# 2d.py ver 0.1 20200507
# 2d.py ver 0.2 20200509

import numpy as np
import cv2
import os

size = 50  # 1セルの幅（描画にしか関係ない）
amo = 8  # セルの縦横の数（初期10）
wait = 0  # 0で毎回ユーザからの操作待ち、1以上でその秒数待つ（描画）
goal_x = 1  # ゴールの座標x※0.2追記始終点入替
goal_y = 5  # ゴールの座標y※0.2追記始終点入替
start_x = 4  # スタートの座標x（初期9）※0.2追記始終点入替
start_y = 1  # スタートの座標y（初期5）※0.2追記始終点入替
sv_count = 0  # 画像保存用：-1で表示のみ※0.2追記
dirName = 'img'
os.makedirs(dirName, exist_ok=True)

next = []  # 次訪問したいリスト[x,y]
dp = [[[0, 0] for i in range(amo)] for j in range(amo)]  # [cost, visited]

# 白イメージの生成
img = np.full((size*amo+4, size*amo+4, 3), 255, np.uint8)

# グリッド線描画（横余白2px）
def grid():
    for i in range(amo+1):
        pts = np.array([[i*size+2, 0+2], [i*size+2, amo*size+2]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 0, 0), 1)
        pts = np.array([[0+2, i*size+2], [amo*size+2, i*size+2]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (0, 0, 0), 1)

# 塗りつぶし
def rect(stx, sty, col):
    x = stx * size
    y = sty * size
    cv2.rectangle(img, (x+4, y+4), (x+size, y+size), color=col, thickness=-1)

# 文字
def chara(x, y):
    cv2.putText(img, str(dp[x][y][0]), ((int)((x+0.1)*size), (int)((y+0.8)*size)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), thickness=1)

# 線
def lin(x1, y1, x2, y2):
    sz = 2+(int)(size/2)
    cv2.line(img, (x1*size+sz, y1*size+sz), (x2*size+sz, y2*size+sz),
             (0, 0, 0), thickness=1, lineType=cv2.LINE_AA)

#表示/保存 sv_count=show(sv_count)で呼び出し（定型）※0.2追記
def show(cnt):
    if cnt == -1:
        cv2.imshow('image', img)
        cv2.waitKey(wait)
        return -1
    else:
        cv2.imwrite(dirName+'/imwrite'+str(cnt)+'.jpg', img)
        return cnt+1

def startInit(x, y):
    col = (0, 0, 255)
    dp[x][y][1] = 1  # Startはvisited:=1
    rect(x, y, col)
    next.append([x, y])

def goalInit(x, y):
    col = (5, 155, 255)
    dp[x][y][1] = 2  # Goalはvisited:=2
    rect(x, y, col)

def obstInit(x1, y1, x2, y2):
    col = (128, 128, 128)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            dp[i][j][1] = 6  # Obstはvisited:=6
            rect(i, j, col)

# Init
grid()
startInit(goal_x, goal_y)
goalInit(start_x, start_y)
obstInit(2, 3, 3, 6)  # 障害物
sv_count = show(sv_count)

def search(stx, sty):
    rect(stx, sty, (255, 204, 51))  # 探索済み塗色
    chara(stx, sty)  # 探索済み距離表示
    for i in range(-1, 2):
        x = stx+i
        if(x < 0 or x >= amo):  # 範囲外
            continue
        for j in range(-1, 2):
            y = sty + j
            if (i % 2 == 1 and j % 2 == 1):  # 以下2行追記（斜めスキップ）
                continue
            if(y < 0 or y >= amo):  # 範囲外
                continue
            elif(x == stx and y == sty):  # 自分自身
                continue
            elif(dp[x][y][1] % 5 == 1):  # スタート(1)または障害物(6)または訪問済み(11)または訪問済みゴール(16)
                continue
            elif(dp[x][y][1] == 2):  # ゴール(2)
                dp[x][y] = [dp[stx][sty][0]+1, 16]
                chara(x, y)
                continue
            dp[x][y] = [dp[stx][sty][0]+1, 11]  # 訪問済み
            rect(x, y, (180, 130, 70))
            next.append([x, y])  # 次訪問リストに追加

while(len(next) != 0):
    search(next[0][0], next[0][1])
    sv_count = show(sv_count)
    cv2.waitKey(wait)
    del next[0]

route = [[] for i in range(dp[start_x][start_y][0])]

def searchRoute(glx, gly):
    flag = 0
    for i in range(-1, 2):
        x = glx-i
        if(x < 0 or x >= amo):  # 範囲外
            continue
        for j in range(-1, 2):
            y = gly-j
            if(y < 0 or y >= amo):  # 範囲外
                continue
            elif(x == glx and y == gly):  # 自分自身
                continue
            elif(dp[x][y][1] == 6):  # 障害物(6)
                continue
            elif(dp[glx][gly][0]-1 != dp[x][y][0]):
                continue
            # rect(x,y,(255,204,255))
            if([x, y] not in route[dp[x][y][0]]):
                route[dp[x][y][0]].append([x, y])
            lin(glx, gly, x, y)
            return -1  # 追記（1通りを選ぶため）


searchRoute(start_x, start_y)

for i in range(dp[start_x][start_y][0]-1, 0, -1):
    for elm in route[i]:
        sv_count = show(sv_count)
        searchRoute(elm[0], elm[1])
        break  # 追記（1通りに絞るため）

cv2.imshow('image', img)
print(dp)
print("route")
print(route)
cv2.waitKey(0)  # 入れ替え
cv2.destroyAllWindows()
