import numpy as np
import norminput
import dijkstra
import Sci

print("\n========================================")
print("  play Ver. 1.0 (20200708)")
print("========================================\n")


print("現在地の座標を入力：")
start_x = int(input("x:"))
start_y = int(input("y:"))
start_z = int(input("z:"))

print("目的地の座標を入力：")
dist_x = int(input("x:"))
dist_y = int(input("y:"))
dist_z = int(input("z:"))

'''
if (start_z > dist_z):
    search_z = start_z
else:
    search_z = dist_z
'''

obst = []
obst_count = 0

'''
for i in range(norminput.count_x):
    for j in range(norminput.count_y):
        if norminput.data[i][j][0] >= search_z:
            obst.append((i, j)) #高度 search_z におけるobst（2次元）
'''

for i in range(norminput.count_x):
    for j in range(norminput.count_y):
        if norminput.data[i][j][0] != 0:
            obst.append([])
            obst[obst_count].append([i, j, 0])
            obst[obst_count].append([i, j, int(norminput.data[i][j][0]) + 1])
            obst_count += 1

#print(obst)

s = Sci.SciSearch([50, 50, 50], [start_x, start_y, start_z], [dist_x, dist_y, dist_z], obst, 1) #(サイズ,始点,終点,障害物,モード)

'''
d = dijkstra.Dijkstra(norminput.count_x, (start_x, start_y), (dist_x, dist_y), dist_z - start_z, obst) #縦横, start, dist, 高度差, obst
d.search()
print(d.routeHeight)
'''
