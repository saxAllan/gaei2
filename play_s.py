import numpy as np
import math
import norminput
import Sci

print("\n========================================")
print("  play Ver. 1.3 (20200722)")
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
        if 0 < i and i < norminput.count_x-1 and 0 < j and j < norminput.count_y-1:
            tmp = []
            tmp_index = []
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                   tmp.append(norminput.data[i + ii][j + jj][0])
                   tmp_index.append([i + ii, j + jj])
            max_index = tmp.index(max(tmp))
            if math.ceil(norminput.data[tmp_index[max_index][0]][tmp_index[max_index][1]][0]) != 0:
                obst.append([i, j, math.ceil(norminput.data[tmp_index[max_index][0]][tmp_index[max_index][1]][0])])
        elif norminput.data[i][j][0] != 0:
            obst.append([i, j, math.ceil(norminput.data[i][j][0])])

s = Sci.SciSearch([50, 50, 50], [start_x, start_y, start_z], [dist_x, dist_y, dist_z], obst, norminput.filename_i) #(サイズ,始点,終点,障害物,モード)

path = s.search()


#ここから元play_n
print("VRMLデータに経路情報を記録しています．．．")
out = ""
for i in range(len(path)):
    out += str(path[i][0])+" "
    out += str(path[i][1])+" "
    out += str(path[i][2])+"\n"

f = open("route.txt", mode="w")
f.write(out)
f.close()
print("route.txt に追記しました")
