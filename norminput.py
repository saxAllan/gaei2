#読み込み
#最終的なデータはdata[][]

print("\n========================================")
print("  norminput Ver. 3.6 (20200723)")
print("========================================\n")

from operator import itemgetter

#読み込み
filename_i = input("入力ファイル名（拡張子は不要）：")
seikika = input("正規化しますか？（Y/N）：")
print(filename_i + ".datを読み込んでいます...  ")
f = open(filename_i + ".dat", "r")
lines = f.readlines()
orgdata = []
for i in lines:
    orgdata.append(list(map(float, i.split())))
f.close()
size_org = len(orgdata)
print("読込完了 (", size_org, "行)")
b = sorted(orgdata, key=itemgetter(0))

bottom = orgdata[0][1]
top = orgdata[size_org-1][1]
left = b[0][0]
right = b[len(b)-1][0]
delete = []

#正規化処理
if seikika == "Y" or seikika == "y":
    while(1):
        for i in range(len(orgdata)):
            if orgdata[i][0] == left or orgdata[i][0] == right or orgdata[i][1] == bottom or orgdata[i][1] == top:
                delete.append(i)
        for i in range(len(delete)):
            orgdata.pop(delete[i]-i)

        # 座標カウント
        y = orgdata[0][1]
        i = 0
        j = 0
        count_x = 0
        count_y = 0
        while orgdata[i][1] == y:
            count_x += 1
            i += 1
        count_y = len(orgdata) // count_x
        data = []
        for i in range(count_x):
            data.append([])

        size_org = len(orgdata)

        # 正規化チェック
        print("x=", count_x, "y=", count_y)
        if count_x * count_y == size_org:
            print("正規化処理完了")
            break
        else:
            print("正規化処理に失敗しましたが、続行します")
            from operator import itemgetter
            b = sorted(orgdata, key=itemgetter(0))

            bottom = orgdata[0][1]
            top = orgdata[len(orgdata)-1][1]
            left = b[0][0]
            right = b[len(b)-1][0]
            delete = []
            #while ここまで
else:
    # 座標カウント
    y = orgdata[0][1]
    i = 0
    j = 0
    count_x = 0
    count_y = 0
    while orgdata[i][1] == y:
        count_x += 1
        i += 1
    count_y = len(orgdata) // count_x
    data = []
    for i in range(count_x):
        data.append([])

    size_org = len(orgdata)

    # 正規化チェック
    print("x=", count_x, "y=", count_y)
    if count_x * count_y == size_org:
        print("正規化処理をスキップしました\nこのデータは正規化されています")
    else:
        print("正規化処理をスキップしましたが、正規化されていない可能性があります")


#2次元配列化
print("二次元配列化処理中...")
for i in range(count_y):
    for j in range(count_x):
        temp = float(orgdata[(i * count_x) + j][2])
        data[j].append([])
        data[j][i].append(temp)
        #data[j][i].append(1)
    print("\r", i + 1, "/", count_y, "   ", end="")
print("処理完了")
print("標高データ読み取り中")
alt =[]
for i in range(count_x):
    for j in range(count_y):
        alt.append(data[i][j][0])
print("処理完了")
