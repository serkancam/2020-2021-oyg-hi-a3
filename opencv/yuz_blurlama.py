import cv2
import numpy as np
import os
casc_yol = os.path.join(os.getcwd(),"opencv","haarcascade_frontalface_alt.xml")
yuz_casc = cv2.CascadeClassifier(casc_yol)
cap = cv2.VideoCapture(-1)
while True:
    ret,resim= cap.read()
    
    griTon = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    yuzler = yuz_casc.detectMultiScale(griTon, 1.3, 7)
    for (x, y, w, h) in yuzler:
        cv2.rectangle(resim, (x, y), (x + w, y + h), (0, 255, 0), 2)
        parca = resim[y:y+h,x:x+w]
        parca = cv2.GaussianBlur(parca,(109,109),0)
        resim[y:y+h,x:x+w]=parca
    cv2.imshow('yuzler', resim)
    if cv2.waitKey(40)==27:
        break
cv2.destroyAllWindows()
cap.release()