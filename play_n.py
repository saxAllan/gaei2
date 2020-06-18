import numpy as np
#import draw
import dijkstra

d = dijkstra.Dijkstra(20, (0, 0), (8, 9), 20, [(2, 2), (2, 3)])
d.search()
print(d.routeHeight)

out=""
for i in range(len(d.routeHeight)):
    print("\r",i,end="  ")
    out += str(d.routeHeight[i][0])+" "
    out += str(d.routeHeight[i][1])+" "
    out += str(d.routeHeight[i][2])+"\n"

f=open("route.txt",mode="w")
f.write(out)
f.close()
print("route.txt に追記しました")