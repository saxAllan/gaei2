import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib.patches import Polygon
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
import math

#壁定義
wall1 = np.array([[0, 0], [100, 0], [100, 400], [400, 400],[400,200],[500,200],[500,500],[0 ,500]])
wall2 = np.array([[200, 0], [700, 0], [700, 500], [600, 500],[600,100],[300,100],[300,300],[200,300]])

#フィールド生成
fig, ax = plt.subplots()
ax.set_xlim([0, 700]) #[min,max]
ax.set_ylim([0, 500])
ax.set_aspect('equal')
ax.add_patch(Polygon(wall1)) #壁
ax.add_patch(Polygon(wall2))

#開始終了地点
start = (50, 50)
distination = (450, 450)
#tilt=(450-50) #接触方式でやろうとした残骸


#内外判定
#points = [(150.5, 150.5), (250, 70)]
orgpoints=[] #全ての点を定義
for i in range(700):
    for j in range(500):
        orgpoints.append((i, j))
        
serching_points=[]

for i, pt in enumerate(orgpoints):
    if (cv2.pointPolygonTest(wall1, pt, False) < 0) and (cv2.pointPolygonTest(wall2, pt, False) < 0): # 点 pt がポリゴンに含まれないとき
        serching_points.append(pt)
#print(serching_points)

#接続判定
pointlist = []
for i, pt in enumerate(serching_points):
    pointlist.append(list(pt)) #タプルをリストへ
#print(pointlist)

print("処理開始")
temp = []
for i in range(len(pointlist)-1):
    if pointlist[i + 1][0] == pointlist[i][0] and pointlist[i + 1][1] == pointlist[i][1]+1:
        #print("前")
        temp.append([i, i + 1, 1.0])

    for j in range(i + 1, len(pointlist) - 1):
        if pointlist[j][0] == pointlist[i][0]+1 and pointlist[j][1] == pointlist[i][1]:
            #print("入")
            temp.append([i, j, 2.0])
            if pointlist[j + 1][0] == pointlist[i][0] + 1 and pointlist[j + 1][1] == pointlist[i][1] + 1:
                temp.append([i, j + 1, math.sqrt(2)])
            break
        elif pointlist[j][0] == pointlist[i][0] + 2:
            break
edge = np.array(temp)
print(edge)
eda = len(temp)
chouten = len(pointlist)


graph = csr_matrix((edge[2], (edge[:2] - 1)), (eda, eda))

#plt.show関連
#ax.scatter(pt[:1], pt[1:], color=color) #タプルを受けて、点を表示
plt.xticks(color="None") #x軸の文字を消す
plt.yticks(color="None")
plt.tick_params(length=0) #軸の目盛りを消す
plt.show()