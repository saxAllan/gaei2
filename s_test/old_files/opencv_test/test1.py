import numpy as np
import cv2

img = cv2.imread('./test.png', 0)

cv2.imshow('image', img)
cv2.waitKey(4000)
cv2.destroyAllWindows()
