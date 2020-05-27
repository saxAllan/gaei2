#divide (now developing)

import numpy as np
import math
import yuki2d

amo = 4 # セルの縦横の値 (org=500)
height = 4  # セルの高さの値
goal_x = 3  # ゴールの座標x (org=470)
goal_y = 3  # ゴールの座標y (org=470)
goal_z = 3 # ゴールの座標z
start_x = 0
start_y = 0
start_z = 0
area_size = 2  # 分割時の縦横 (org=50)

dp = np.zeros((amo, amo, height, 2), dtype=int)
#print(dp)

dp[start_x][start_y][start_z][1] = 1
dp[goal_x][goal_y][goal_z][1] = 2

#50x50の100エリアに分割
area_amo = math.ceil(amo / area_size) # area縦横の数 (= size)
#div = np.zeros((amo // 50, amo // 50, 2), dtype=int) # エリア分け

#S/G座標がどのエリアか
area_goal_x = goal_x // area_size
area_goal_y = goal_y // area_size
area_start_x = start_x // area_size
area_start_y = start_y // area_size

area_route_org = yuki2d.search_2d(area_amo, area_goal_x, area_goal_y, area_start_x, area_start_y) # エリアの経路探索
#print(area_route_org)

# yuki2dからの戻り値をnpに変換
order = len(area_route_org)
area_route = np.zeros((order, 2), dtype=int)
for i in range(order):
    area_route[i][0] = area_route_org[i][0][0]
    area_route[i][1] = area_route_org[i][0][1]
print(area_route)

#高度差をエリアでならす
z_diff_area = (goal_z - start_z)
current_z = np.zeros(order, dtype=int)
for i in range(order-1):
    current_z[i] = start_z + math.ceil(z_diff_area * (i + 1) / order)
current_z[order - 1] = goal_z
print("alt:", current_z)  # current_zには各エリア最終点における高度を格納（ただし、S/Gのエリア内における位置は考慮しない）

# エリアを切り出し
cut_area = []
for i in range(order):
    temp_x = area_size * area_route[order - i - 1][0]
    temp_y = area_size * area_route[order - i - 1][1]
    cut_area.append(dp[temp_x: (temp_x + area_size), temp_y: (temp_y + area_size)]) # <np.array>を要素として持つ<標準リスト>
#print(cut_area)

