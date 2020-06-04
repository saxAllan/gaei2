import numpy as np
import cv2
import os


class Draw:
    def __init__(self, width, n):
        self.img = np.full((width*n+4, width*n+4, 3), 255, np.uint8)
        self.width = width
        self.n = n

        self.sv_count = -1  # 画像保存用：-1で表示のみ※0.2追記
        self.wait = 0  # 0で毎回ユーザからの操作待ち、1以上でその秒数待つ（描画）
        self.dirName = 'img'
        os.makedirs(self.dirName, exist_ok=True)

    # 表示/保存 sv_count=show(sv_count)で呼び出し（定型）※0.2追記
    def show(self):
        if self.sv_count == -1:
            cv2.imshow('image', self.img)
            cv2.waitKey(self.wait)
            self.sv_count = -1
        else:
            cv2.imwrite(self.dirName+'/imwrite' +
                        str(self.sv_count)+'.jpg', self.img)
            self.sv_count += 1
        cv2.destroyAllWindows()

    # 塗りつぶし
    def drawRect(self, cd, col):
        x = cd[0] * self.width+(int)(self.width/2)
        y = cd[1] * self.width+(int)(self.width/2)
        cv2.circle(self.img, (x, y), (int)
                   (self.width/4), col, thickness=-1)

    # 線
    def drawLine(self, cd1, cd2, col):
        x1 = cd1[0] * self.width+(int)(self.width/2)
        y1 = cd1[1] * self.width+(int)(self.width/2)
        x2 = cd2[0] * self.width+(int)(self.width/2)
        y2 = cd2[1] * self.width+(int)(self.width/2)
        cv2.line(self.img, (x1,y1), (x2,y2),    col, thickness=1, lineType=cv2.LINE_AA)

    def drawChara(self, cd, string):
        cv2.putText(self.img, string, ((int)((cd[0]+0.2)*self.width), (int)((cd[1]+1)*self.width)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), thickness=1)

    def drawObst(self, cd, col):
        x = cd[0] * self.width
        y = cd[1] * self.width
        cv2.rectangle(self.img, (x-(int)(self.width/2), y-(int)(self.width/2)), (x+(int)(self.width*3/2), y+(int)(self.width*3/2)), color=col, thickness=-1)