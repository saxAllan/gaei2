import numpy as np
#import draw
import dijkstra

d = dijkstra.Dijkstra(20, (0, 0), (8, 9), 20, [(2, 2), (2, 3)])
d.search()
print(d.routeHeight)
