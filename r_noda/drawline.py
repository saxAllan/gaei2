import cv2  #OpenCVのインポート
import numpy as np  #numpyをnpという名前でインポート

#400要素X600要素X3要素で全要素の値が255(白)の3次元配列を生成しオブジェクトimgに代入
img=np.ones((400, 500, 3), np.uint8)*255 


cv2.line(img,(0,0),(0,400),(255,0,0),3)
cv2.line(img,(0,0),(300,0),(255,0,0),3)
cv2.line(img,(300,0),(300,200),(255,0,0),3)
cv2.line(img,(300,200),(400,200),(255,0,0),3)
cv2.line(img,(400,200),(400,0),(255,0,0),3)
cv2.line(img,(400,0),(500,0),(255,0,0),3)
cv2.line(img,(500,0),(500,400),(255,0,0),3)
cv2.line(img,(0,400),(100,400),(255,0,0),3)
cv2.line(img,(100,400),(100,200),(255,0,0),3)
cv2.line(img,(100,200),(200,200),(255,0,0),3)
cv2.line(img,(200,200),(200,400),(255,0,0),3)
cv2.line(img,(200,400),(500,400),(255,0,0),3)

cv2.imwrite("line",img) #別ウィンドウを開き(ウィンドウ名 "line")オブジェクトimgを表示
             
cv2.waitKey(0) #キー入力待ち
cv2.destroyAllWindows() #ウインドウを閉じる