import cv2
import os
import numpy as np

cd  = os.getcwd()
image_path = os.path.join(cd,"opencv","images","chp2","zebrasmall.png")
image_o = cv2.imread(image_path)
h,w,c = image_o.shape
center = (w//2,h//2)
angle = 45
scale = 1.0
# 45 derece merkezden döndürmek için işlemler
r_m1 = cv2.getRotationMatrix2D(center,angle,scale)
image_r1 = cv2.warpAffine(image_o,r_m1,(w,h))
# 30 derece en sol üst köşeden döndürme
r_m2 = cv2.getRotationMatrix2D((0,0),-30,1.0)
image_r2 =  cv2.warpAffine(image_o,r_m2,(w,h))
cv2.imshow("orjinal",image_o)
cv2.imshow("Rotate1",image_r1)
cv2.imshow("Rotate2",image_r2)
cv2.waitKey(0)
