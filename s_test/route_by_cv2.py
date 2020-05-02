import matplotlib.pyplot as plt
import numpy as np
import cv2
from matplotlib.patches import Polygon

#面を生成
wall1 = np.array([[100, 0], [200, 0], [200, 400], [100, 400]])
wall2 = np.array([[300, 100], [400, 100], [400, 500], [300, 500]])
print(wall1)
print(wall2)
