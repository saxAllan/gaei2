import numpy as np
import norminput
import dijkstra


print("\n========================================")
print("  play Ver. 0.1 (20200614)")
print("========================================\n")


print("現在地の座標を入力：")
start_x = int(input("x:"))
start_y = int(input("y:"))
start_z = int(input("z:"))

print("目的地の座標を入力：")
dist_x = int(input("x:"))
dist_y = int(input("y:"))
dist_z = int(input("z:"))

obst = []
for i in range(norminput.count_x):
    for j in range(norminput.count_y):
        for k in range(int(norminput.data[i][j][0]) + 1):
            obst.append((i, j, k))

d = dijkstra.Dijkstra(norminput.count_x, (start_x, start_y), (dist_x, dist_y), dist_z - start_z, obst) #縦横, start, dist, 高度差, obst
d.search()
print(d.routeHeight)
