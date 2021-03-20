import cv2
import os 
import numpy as np 
resim_yolu = os.path.join(os.getcwd(),"opencv","images","chp2","elmalar.jpeg")
resim = cv2.imread(resim_yolu)
resim = cv2.bilateralFilter(resim,11,50,50)
print(resim.shape)
gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
print(gri.shape)
sbResim = cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)
# t,sbResim = cv2.adaptiveThreshold(gri,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)
cv2.imshow("sbResim",sbResim)
#konturlar
konturlar,_ = cv2.findContours(sbResim,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(len(konturlar))
print(konturlar[0][0][0])
print(konturlar[0][1][0])
print(konturlar[0][2][0])
print(konturlar[0][3][0])
x1=konturlar[0][0][0]
x2=konturlar[0][1][0]
x3= konturlar[0][2][0]
x4= konturlar[0][3][0]
cv2.circle(resim,tuple(x1),5,(255,0,0),-1)
cv2.circle(resim,tuple(x2),5,(255,0,0),-1)
cv2.circle(resim,tuple(x3),5,(255,0,0),-1)
cv2.circle(resim,tuple(x4),5,(255,0,0),-1)
cv2.imshow("resim son",resim)
# konturların çizdirilmesi
for kontur in konturlar:
    deger =cv2.approxPolyDP(kontur,0.009*cv2.arcLength(kontur,True),True)
    cv2.drawContours(resim,[deger],0,(0,0,255),2)
cv2.imshow("resim konturlu",resim)
cv2.waitKey(0)