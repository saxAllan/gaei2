#欠損点削除(低)
print("\n========================================")
print("  mpointsl Ver. 1.5 (20191213)")
print("========================================\n")

import norminput

data2=norminput.data[:]
for i in range(norminput.count_y):
    for j in range(norminput.count_x):
        if norminput.data[j][i][0]+9999<1:
                norminput.data[j][i][0]=norminput.data[j-1][i][0]
for i in range(norminput.count_x):
    for j in range(norminput.count_y):
        if data2[i][j][0]+9999<1:
                data2[i][j][0]=data2[i][j-1][0]
for i in range(norminput.count_y):
    for j in range(norminput.count_x):
        if norminput.data[j][i][0]>data2[j][i][0]:    
                norminput.data[j][i][0]=data2[j][i][0]

for i in range(norminput.count_y):
    for j in range(1,norminput.count_x-1):
        if norminput.data[j][i][0]-norminput.data[j-1][i][0]>=5 and norminput.data[j][i][0]-norminput.data[j+1][i][0]>=5:
            norminput.data[j][i][0]=(norminput.data[j-1][i][0]+norminput.data[j+1][i][0])/2

for i in range(norminput.count_x):
    for j in range(1,norminput.count_y-1):
        if norminput.data[i][j][0]-norminput.data[i][j-1][0]>=5 and norminput.data[i][j][0]-norminput.data[i][j+1][0]>=5:
            norminput.data[i][j][0]=(norminput.data[i][j-1][0]+norminput.data[i][j+1][0])/2

print("欠損点処理完了")
