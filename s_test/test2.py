import cv2
import numpy as np

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
img = np.full((500, 500, 3), 64, dtype=np.uint8)

cv2.line(img, (100, 400), (100, 100), (255, 255, 255))
cv2.line(img, (100, 100), (300, 100), (255, 255, 255))
cv2.line(img, (300, 100), (300, 300), (255, 255, 255))
cv2.line(img, (200, 200), (200, 400), (255, 255, 255))
cv2.line(img, (200, 400), (400, 400), (255, 255, 255))
cv2.line(img, (400, 400), (400, 100), (255, 255, 255))

cv2.imshow('test',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
