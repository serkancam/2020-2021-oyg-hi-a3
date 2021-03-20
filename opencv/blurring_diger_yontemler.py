import cv2
import os
import numpy as np

cd = os.getcwd()
image_path = os.path.join(cd,"opencv","images","chp2","salt-pepper.jpg")
while True:
    image = cv2.imread(image_path)
    # h,w,c=image.shape
    # print(c)
    image =  cv2.resize(src=image,dsize=None,fx=0.7,fy=0.7)
    #orijinal resim
    cv2.imshow("orijinal resim",image)
    # 7*7 lük piksellere bölünmüş resmin yumuşatılmış haline--> blurm7
    blurm7 = cv2.medianBlur(image,7)
    cv2.imshow("blurm7",blurm7)
    # mean filtering
    blur_mean =cv2.blur(image,(7,7))
    cv2.imshow("blur_mean",blur_mean)
    # gaussian blur
    blur_gaussian = cv2.GaussianBlur(image,(7,7),0)
    cv2.imshow("blur_gaussian",blur_gaussian)
    # bilateral filter
    blur_bilateral = cv2.bilateralFilter(image,7,150,150)
    cv2.imshow("blur_bilateral",blur_bilateral)
    gelen=cv2.waitKey(0)
    if gelen==ord('a'):
       break