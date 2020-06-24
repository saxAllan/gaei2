import numpy as np
#import draw
import dijkstra

d = dijkstra.Dijkstra(50, (1, 1), (30, 20), 0, [(2, 2), (2, 3),(20,10),(15,7)])
d.search()
print(d.routeHeight)
