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

obst = []
obst_count = 0

for i in range(norminput.count_x):
    for j in range(norminput.count_y):
        if norminput.data[i][j][0] != 0:
            obst.append([])
            obst[obst_count].append([i, j, 0])
            obst[obst_count].append([i, j, int(norminput.data[i][j][0]) + 1])
            obst_count += 1

s = Sci.SciSearch([50, 50, 50], [start_x, start_y, start_z], [dist_x, dist_y, dist_z], obst, 1) #(サイズ,始点,終点,障害物,モード)

path = s.search()


#ここから元play_n
out = ""
for i in range(len(path)):
    print("\r", i, end="  ")
    out += str(d.routeHeight[i][0])+" "
    out += str(d.routeHeight[i][1])+" "
    out += str(d.routeHeight[i][2])+"\n"

f = open("route.txt", mode="w")
f.write(out)
f.close()
print("route.txt に追記しました")
