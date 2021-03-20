import cv2
import numpy as np 
import time
from datetime import datetime

cap = cv2.VideoCapture(-1)# eğer windows olsaydı 0 yazacaktık.
ret1,frame1 = cap.read()
ret2,frame2 = cap.read()
while cap.isOpened():
    # hareket tespiti
    fark = cv2.absdiff(frame1,frame2)
    gri = cv2.cvtColor(fark,cv2.COLOR_BGR2GRAY)
    bulanik = cv2.GaussianBlur(gri,(5,5),0)
    t,sbResim = cv2.threshold(bulanik,20,255,cv2.THRESH_BINARY)
    yayilmis=cv2.dilate(sbResim,None,iterations=3)
    konturlar,x=cv2.findContours(yayilmis,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print(len(konturlar))
    for kontur in konturlar:
        (x,y,w,h) = cv2.boundingRect(kontur)
        if cv2.contourArea(kontur)<1600:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"Hareket algilandi\n"+str(datetime.now()),(10,30),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255))
        
    # hareket tespit sonu
    # görüntleme
    # cv2.imshow("frame2",frame2)
    cv2.imshow("frame1",frame1)
    # cv2.imshow("fark",fark)
    # cv2.imshow("fark-gri",gri)
    # cv2.imshow("fark-gri-blur",bulanik)
    # cv2.imshow("fark-gri-blur-binarizaion",sbResim)
    # cv2.imshow("fark-gri-blur-binarizaion",sbResim)
    # cv2.imshow("fark-gri-blur-binarizaion-dilate",yayilmis)
    frame1 = frame2
    # time.sleep(0.5)
    ret2,frame2 = cap.read()
    if cv2.waitKey(40)==27:#27 escape tuşunun ascii değeri
        break

cv2.destroyAllWindows()
cap.release()