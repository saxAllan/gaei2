#2d.py ver 0.1 20200507

import numpy as np
#import cv2

#size = 20  # 1セルの幅（描画にしか関係ない）
amo = 4  # セルの縦横高さの値（初期4）
#wait = 0  # 0で毎回ユーザからの操作待ち、1以上でその秒数待つ（描画）
goal_x = 4  # ゴールの座標x
goal_y = 4  # ゴールの座標y
goal_z = 4  # ゴールの座標z
start_x = 0
start_y = 0
start_z = 0

next = []  # 次訪問したいリスト[x,y]
dp = [[[[0, 0] for i in range(amo)] for j in range(amo)] for k in range(amo)]  # [cost, visited]

#削除01

def startInit(x, y, z):
    dp[x][y][z][1] = 1  # Startはvisited:=1
    next.append([x, y])

def goalInit(x, y, z):
    dp[x][y][z][1] = 2  # Goalはvisited:=2

def obstInit(x1, y1, z1, x2, y2, z2):
    for i in range(x1, x2+1):
        for j in range(y1, y2 + 1):
            for k in range(z1, z2 + 1):
                dp[i][j][k][1] = 6  # Obstはvisited:=6

# Init
startInit(start_x, start_y, start_z)
goalInit(goal_x, goal_y, goal_z)
obstInit(1, 1, 1, 2, 2, 2)  # 障害物

def search_sub(x, y, z):
    if dp[x][y][z][1] != 2: 
        dp[x][y][z] = [dp[x][y][z][0] + 1, 11]  # 訪問済み
        next.append([x, y, z])  # 次訪問リストに追加
    else:
        dp[x][y][z] = [dp[x][y][z][0] + 1, 16] # 訪問済みゴール(16)

def search(stx, sty, stz):
    x = stx
    y = sty
    z = stz
    #1
    x += 1
    if (x < amo and dp[x][y][z][1] % 5 != 1): # 範囲 & スタート(1)または障害物(6)または訪問済み(11)または訪問済みゴール(16)
        search_sub(x, y, z)
    #2
    x -= 2
    if (x >= 0 and dp[x][y][z][1] % 5 != 1): # 範囲 & スタート(1)または障害物(6)または訪問済み(11)または訪問済みゴール(16)
        search_sub(x, y, z)
    #3
    x += 1
    y -= 1
    if (y >= 0  and dp[x][y][z][1] % 5 != 1): # 範囲 & スタート(1)または障害物(6)または訪問済み(11)または訪問済みゴール(16)
        search_sub(x, y, z)
    #4
    y += 2
    if (y < amo and dp[x][y][z][1] % 5 != 1): # 範囲 & スタート(1)または障害物(6)または訪問済み(11)または訪問済みゴール(16)
        search_sub(x, y, z)
    #5
    y -= 1
    z -= 1
    if (z >= 0 and dp[x][y][z][1] % 5 != 1): # 範囲 & スタート(1)または障害物(6)または訪問済み(11)または訪問済みゴール(16)
        search_sub(x, y, z)
    #6
    z += 2
    if (z < amo and dp[x][y][z][1] % 5 != 1): # 範囲 & スタート(1)または障害物(6)または訪問済み(11)または訪問済みゴール(16)
        search_sub(x, y, z)   

while(len(next) != 0):
    search(next[0][0], next[0][1], next[0][2])
    del next[0]

route = [[] for i in range(dp[goal_x][goal_y][goal_z][0])]

def searchRoute(glx, gly, glz):
    flag = 0
    for i in range(-1, 2):
        x = glx - i
        if(x < 0 or x >= amo):  # 範囲外
            continue
        for j in range(-1, 2):
            y = gly - j
            if(y < 0 or y >= amo):  # 範囲外
                continue
            for k in range(-1, 2):
                z = glz - k
                if (z < 0 or z >= amo):
                    continue
                elif(x == glx and y == gly):  # 自分自身
                    continue
                elif(dp[x][y][1] == 6):  # 障害物(6)
                    continue
                elif(dp[glx][gly][0]-1 != dp[x][y][0]):
                    continue
                if([x, y] not in route[dp[x][y][0]]):
                    route[dp[x][y][0]].append([x, y])
                return -1  # 追記（1通りを選ぶため）

searchRoute(goal_x, goal_y, goal_z)

for i in range(dp[goal_x][goal_y][goal_z][0]-1, 0, -1):
    for elm in route[i]:
        searchRoute(elm[0], elm[1], elm[2])
        break  # 追記（1通りに絞るため）

print(dp)
print("route")
print(route)