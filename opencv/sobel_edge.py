import cv2
import numpy as np 
import os

resim_yolu = os.path.join(os.getcwd(),"opencv","images","chp2","sudoku.jpg")
resim = cv2.imread(resim_yolu)
cv2.imshow("resim",resim)
print(resim.shape)
#gri tonlamalı resim
gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
print(gri.shape)
gri = cv2.bilateralFilter(gri,7,50,50)
cv2.imshow("gri blur",gri)
# sobel x
sobelx = cv2.Sobel(gri,cv2.CV_64F,1,0,ksize=3)
sobelx = np.uint8(np.absolute(sobelx)) 
print(sobelx)
cv2.imshow("sobelx",sobelx)
# sobel y
sobely = cv2.Sobel(gri,cv2.CV_64F,0,1,ksize=3)
sobely = np.uint8(np.absolute(sobely)) 
print(sobely)
cv2.imshow("sobely",sobely)
# laplace 
laplace = cv2.Laplacian(gri,cv2.CV_64F)
laplace = np.uint8(np.absolute(laplace))
cv2.imshow("laplace",laplace)
# canny
canny = cv2.Canny(gri,50,170)
cv2.imshow("canny",canny)
print(laplace)
cv2.waitKey(0)