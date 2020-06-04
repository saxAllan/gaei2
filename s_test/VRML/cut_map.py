import numpy as np

filename_i = input("入力ファイル名（拡張子は不要）：")
filename_o = input("出力ファイル名（拡張子は不要）：")

print(filename_i + ".datを読み込んでいます...  ")
f = open(filename_i + ".dat", "r")
lines = f.readlines()
orgdata = []
for i in lines:
    orgdata.append(list(map(float, i.split())))
f.close()
size_org = len(orgdata)
print("読込完了 (", size_org, "行)")

cnt=1
while(1):
    if orgdata[cnt][1]!=orgdata[0][1]:
        break
    cnt+=1

n=int(input("データ数:"))

a=[0]*n*n

s=int(input("始点の添え字:"))
#print(s)
while (s+1)%cnt>cnt-(n-1):
    s=int(input("やり直し:"))


cnt1=0
cnt2=0
while(cnt1<n*n):
    #print(cnt1,s+cnt2)
    a[cnt1]=orgdata[s+cnt2]
    cnt1+=1
    cnt2+=1
    if cnt1%n==0:
        cnt2+=cnt-n

out=str("")
for i in range(len(a)):
    print("\r",i,end="  ")
    out += str(a[i][0])+" "
    out += str(a[i][1])+" "
    out += str(a[i][2])+" "
    #out += str(orgdata[i][3])+" "
    out += str("\n")

f=open(filename_o+".dat",mode="w")
f.write(out)
f.close()
print(filename_o+".dat を出力しました")