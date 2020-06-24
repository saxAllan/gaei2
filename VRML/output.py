print("x座標,y座標,z座標が1行ごとに書かれているtxtファイルを用意してください\n")

filename_i = input("入力ファイル名（拡張子は不要）：")

print(filename_i + ".txtを読み込んでいます...  ")
f = open(filename_i + ".txt", "r")
lines = f.readlines()
orgdata = []
for i in lines:
    orgdata.append(list(map(float, i.split())))
f.close()
size_org = len(orgdata)
print("読込完了 (", size_org, "行)")

with open('UFO.txt', 'r') as f:
    p=f.read()
    q=""
    q+="DEF UFO Transform{\n"
    q+="  translation "
    q+=str(orgdata[0][0])+" "+str(orgdata[0][1])+" "+str(orgdata[0][2])+"\n"
    q+="  rotation 1 0 0 1.570796326794897\n"
    q+=p
out=("\n")
out+=q
out+=str("\n")
out+=("DEF TS3 TimeSensor{\n")
out+=("  cycleInterval 10\n")
out+=("  loop TRUE\n")
out+=("}\n")
out+=("DEF PI2 PositionInterpolator{\n")
out+=("  key[")

for i in range(size_org-1):
    out+=(str(i/(size_org-1))+",")
out+=("1]\n")
out+=("  keyValue[")

for i in range(size_org):
    print("\r",i,end="  ")
    out += str(orgdata[i][0])+" "
    out += str(orgdata[i][1])+" "
    out += str(orgdata[i][2])+","

out+=("]\n")
out+=("}\n")
out+=("ROUTE TS3.fraction_changed TO PI2.set_fraction\n")
out+=("ROUTE PI2.value_changed TO UFO.set_translation\n")
f=open("t500.wrl",mode="a")
f.write(out)
f.close()
print("t500.wrl に追記しました")