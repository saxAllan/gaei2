#マージ・ドロネー・出力
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import numpy as np
import norminput
import mpointsl
#import judgements3
print("\n========================================")
print("  out3 Ver. 2.10 (20200103)")
print("========================================\n")


newdata = []
zdata = []
cdata = []
for i in range(norminput.count_y):
    for j in range(norminput.count_x):
        zdata.append(norminput.data[j][i][0])
        cdata.append(norminput.data[j][i][1])
        newdata.append(j)
        newdata.append(i)
print(norminput.count_x)
print("Delaunay 処理中(多少時間がかかります)")
pts = np.array(newdata).reshape(-1, 2)
ztmp = np.array(zdata)
tri = Delaunay(pts)
newdata = pts.tolist()

temp_len = len(newdata)
for i in range(temp_len):
    newdata[i].append(zdata[i])
pts = np.array(newdata)
fig = plt.figure()
print("Delaunay 処理完了   (len(pts)=", len(pts), "), (len(pts[tri.simplices])=", len(pts[tri.simplices]), ")")

#出力
filename_o = input("出力ファイル名（拡張子は不要）：")
outfile = open(filename_o + '.wrl', 'w')
print(filename_o + ".wrl として出力中...")

start = '#VRML V2.0 utf8\n'
outfile.write(start)
text1 = 'Shape {\ngeometry IndexedFaceSet { \nsolid FALSE\ncoord Coordinate { \npoint [\n'
outfile.write(text1)

temp_len=len(pts)
for i in range(temp_len):
    if i % 10000 == 0:
        print("\rpoint ", i // 10000, "/", temp_len // 10000, end="")
    for j in range(3):
        outfile.writelines(str(pts[i][j]))
        if j == 0 or j == 1:
            space = ' '
            outfile.write(space)
    conma = ',\n'
    outfile.write(conma)
print("   処理完了")

textc = ']\n}\ncoordIndex [\n'
outfile.write(textc)
temp_len=len(pts[tri.simplices])
for i in range(temp_len):
    if i % 10000 == 0:
        print("\rcoordIndex ", i // 10000, "/", temp_len // 10000, end="")
    for j in range(3):
        outfile.writelines(str(tri.simplices[i][j]))
        conma2 = ','
        outfile.write(conma2)
    conma3 = '-1,\n'
    outfile.write(conma3)
print("   処理完了")

#color処理

newdata = pts.tolist()
temp_p = len(newdata)
for i in range(temp_p):
    newdata[i].append(cdata[i])
pts = np.array(newdata)

color1=']\ncolor Color { color [ 1 1 0, 0 1 0 ] }\ncolorIndex [\n'
outfile.write(color1)
num1=1
num0=0
for i in range(temp_len):
    cnt=0
    if i % 10000 == 0:
        print("\rcolor ", i // 10000, "/", temp_len // 10000, end="")
    for j in range(3):
        if pts[tri.simplices[i][j]][3]==1:
               cnt+=1
    if cnt==0:
        outfile.writelines(str(num1))
    else:
        outfile.writelines(str(num0))
    if i<temp_len-1:
        conma2 = ','
        outfile.write(conma2)

text2 = '\n]\ncolorPerVertex FALSE\n}\nappearance Appearance { \nmaterial Material {}\n}\n}\n'
outfile.write(text2)

newdata = pts.tolist()
temp_p = len(newdata)
for i in range(temp_p):
    del newdata[i][3]
pts = np.array(newdata)

print("   処理完了")
#側面
x_max=pts[0][0]
x_min=pts[0][0]
y_max=pts[0][1]
y_min=pts[0][1]
temp_len=len(pts)
rd=0
ld=0
lu=0
for i in range(temp_len):
    if x_max < pts[i][0]:
        x_max=pts[i][0]
        rd=i
    elif x_min > pts[i][0]:
        x_min=pts[i][0]
        ld=i
    if y_max < pts[i][1]:
        y_max=pts[i][1]
        lu=i
    elif y_min > pts[i][1]:
        y_min=pts[i][1]
ru=temp_len-1
text1 = 'Shape {\ngeometry IndexedFaceSet { \nsolid FALSE\ncoord Coordinate { \npoint [\n'
outfile.write(text1)
cnt=0
for i in range(temp_len):
    if pts[i][1]==y_max:
        tmp=i
        if cnt==0:
            for j in range(2):
                outfile.writelines(str(pts[i][j]))
                space = ' '
                outfile.write(space)
            tconma = '-100,\n'
            outfile.write(tconma)
            cnt+=1
        for j in range(3):
            outfile.writelines(str(pts[i][j]))
            if j == 0 or j == 1:
                space = ' '
                outfile.write(space)
        conma = ',\n'
        outfile.write(conma)
for j in range(2):
    outfile.writelines(str(pts[tmp][j]))
    space = ' '
    outfile.write(space)
tconma = '-100,\n'
outfile.write(tconma)
textc = ']\n}\ncoordIndex [\n'
outfile.write(textc)
for i in range(norminput.count_x + 2):
    outfile.writelines(str(i))
    conma2 = ','
    outfile.write(conma2)
conma3 = '-1,\n'
outfile.write(conma3)
print("y_max処理完了")
text2 = ']\n}\nappearance Appearance { \nmaterial\nMaterial {}\n}\n}\n'
outfile.write(text2)

text1 = 'Shape {\ngeometry IndexedFaceSet { \nsolid FALSE\ncoord Coordinate { \npoint [\n'
outfile.write(text1)
cnt=0
for i in range(temp_len):
    if pts[i][0]==x_max:
        tmp=i
        if cnt==0:
            for j in range(2):
                outfile.writelines(str(pts[i][j]))
                space = ' '
                outfile.write(space)
            tconma = '-100,\n'
            outfile.write(tconma)
            cnt+=1
        for j in range(3):
            outfile.writelines(str(pts[i][j]))
            if j == 0 or j == 1:
                space = ' '
                outfile.write(space)
        conma = ',\n'
        outfile.write(conma)
for j in range(2):
    outfile.writelines(str(pts[tmp][j]))
    space = ' '
    outfile.write(space)
tconma = '-100,\n'
outfile.write(tconma)
textc = ']\n}\ncoordIndex [\n'
outfile.write(textc)
for i in range(norminput.count_y + 2):
    outfile.writelines(str(norminput.count_y+1-i))
    conma2 = ','
    outfile.write(conma2)
conma3 = '-1,\n'
outfile.write(conma3)
print("x_max処理完了")
text2 = ']\n}\nappearance Appearance { \nmaterial\nMaterial {}\n}\n}\n'
outfile.write(text2)

text1 = 'Shape {\ngeometry IndexedFaceSet { \nsolid FALSE\ncoord Coordinate { \npoint [\n'
outfile.write(text1)
cnt=0
for i in range(temp_len):
    if pts[i][1]==y_min:
        tmp=i
        if cnt==0:
            for j in range(2):
                outfile.writelines(str(pts[i][j]))
                space = ' '
                outfile.write(space)
            tconma = '-100,\n'
            outfile.write(tconma)
            cnt+=1
        for j in range(3):
            outfile.writelines(str(pts[i][j]))
            if j == 0 or j == 1:
                space = ' '
                outfile.write(space)
        conma = ',\n'
        outfile.write(conma)
for j in range(2):
    outfile.writelines(str(pts[tmp][j]))
    space = ' '
    outfile.write(space)
tconma = '-100,\n'
outfile.write(tconma)
textc = ']\n}\ncoordIndex [\n'
outfile.write(textc)
for i in range(norminput.count_x + 2):
    outfile.writelines(str(norminput.count_x+1-i))
    conma2 = ','
    outfile.write(conma2)
conma3 = '-1,\n'
outfile.write(conma3)
print("y_min処理完了")
text2 = ']\n}\nappearance Appearance { \nmaterial\nMaterial {}\n}\n}\n'
outfile.write(text2)

text1 = 'Shape {\ngeometry IndexedFaceSet { \nsolid FALSE\ncoord Coordinate { \npoint [\n'
outfile.write(text1)
cnt=0
for i in range(temp_len):
    if pts[i][0]==x_min:
        tmp=i
        if cnt==0:
            for j in range(2):
                outfile.writelines(str(pts[i][j]))
                space = ' '
                outfile.write(space)
            tconma = '-100,\n'
            outfile.write(tconma)
            cnt+=1
        for j in range(3):
            outfile.writelines(str(pts[i][j]))
            if j == 0 or j == 1:
                space = ' '
                outfile.write(space)
        conma = ',\n'
        outfile.write(conma)
for j in range(2):
    outfile.writelines(str(pts[tmp][j]))
    space = ' '
    outfile.write(space)
tconma = '-100,\n'
outfile.write(tconma)
textc = ']\n}\ncoordIndex [\n'
outfile.write(textc)
for i in range(norminput.count_y + 2):
    outfile.writelines(str(i))
    conma2 = ','
    outfile.write(conma2)
conma3 = '-1,\n'
outfile.write(conma3)
print("x_min処理完了")
text2 = ']\n}\nappearance Appearance { \nmaterial\nMaterial {}\n}\n}\n'
outfile.write(text2)

#底面
text1 = 'Shape {\ngeometry IndexedFaceSet { \nsolid FALSE\ncoord Coordinate { \npoint [\n'
outfile.write(text1)

for j in range(2):
    outfile.writelines(str(pts[ld][j]))
    space = ' '
    outfile.write(space)
tconma = '-100,\n'
outfile.write(tconma)
for j in range(2):
    outfile.writelines(str(pts[rd][j]))
    space = ' '
    outfile.write(space)
tconma = '-100,\n'
outfile.write(tconma)
for j in range(2):
    outfile.writelines(str(pts[ru][j]))
    space = ' '
    outfile.write(space)
tconma = '-100,\n'
outfile.write(tconma)
for j in range(2):
    outfile.writelines(str(pts[lu][j]))
    space = ' '
    outfile.write(space)
tconma = '-100,\n'
outfile.write(tconma)

textc = ']\n}\ncoordIndex [\n'
outfile.write(textc)
for i in range(4):
    outfile.writelines(str(3-i))
    conma2 = ','
    outfile.write(conma2)
conma3 = '-1,\n'
outfile.write(conma3)
print("底面処理完了")
text2 = ']\n}\nappearance Appearance { \nmaterial\nMaterial {}\n}\n}\n'
outfile.write(text2)

print("処理完了")
print(filename_o, ".wrl としてVRMLファイルを出力しました", sep="")