import numpy as np
import math
import yuki2d

amo = 500 # セルの縦横の値（初期4）
height=100 # セルの高さの値
goal_x = 470  # ゴールの座標x
goal_y = 470  # ゴールの座標y
goal_z = 70  # ゴールの座標z
start_x = 0
start_y = 0
start_z = 0
area_size = 50  # 分割時の縦横

#dp = [[[[0, 0] for i in range(amo)] for j in range(amo)] for k in range(height)]  # [cost, visited]
#print(dp2)

dp = np.zeros((amo, amo, height, 2), dtype=int)
#print(dp)

dp[start_x][start_y][start_z][1] = 1
dp[goal_x][goal_y][goal_z][1] = 2

#50x50の100エリアに分割
area_amo = math.ceil(amo / area_size) # area縦横の数 (= size)
div = np.zeros((amo // 50, amo // 50, 2), dtype=int)
area_goal_x = goal_x // 50
area_goal_y = goal_y // 50
area_start_x = start_x // 50
area_start_y = start_y // 50
#print(area_goal_x, " ", area_goal_y)
area_route = yuki2d.search_2d(area_amo, area_goal_x, area_goal_y, area_start_x, area_start_y)
print(area_route)