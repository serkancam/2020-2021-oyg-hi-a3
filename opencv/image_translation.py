import cv2
import os
import numpy as np

cd = os.getcwd()
image_path = os.path.join(cd,"opencv","images","chp2","zebra.png")
zebra_o = cv2.imread(image_path)
# zebra_r1 = zebra_o.copy()
# zebra_r2 = zebra_o.copy()
h,w = zebra_o.shape[:2]
# h,w,c = zebra_o.shape
# aspect ratio --- en boy oranı 
aspect = w/h

# yeni yükseklik hesaplayalım
h_new  = int(h*0.2)
w_new = int(h_new*aspect)
dimension = (h_new,w_new)
# şimdi zebra_r1 kopyasını yeni boyutu(dimension) ile yeniden boyutlandıralım(resized)
zebra_r1 = cv2.resize(zebra_o,dimension,interpolation=cv2.INTER_AREA)


cv2.imshow("Original",zebra_o)
cv2.imshow("R1",zebra_r1)
cv2.waitKey(0)