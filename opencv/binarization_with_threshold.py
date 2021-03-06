# binarization ikileşitirme
# threshold : eşik değeri
# eşik değeri ile ikileştirme
# görüntü ikileştime sadece gri tonlamalı esimlere uygulanır 
# ikleştirmenin bir ço yolu vardır.
import cv2
import numpy as np
import os 

resim_yolu = os.path.join(os.getcwd(),"opencv","images","chp2","scanned_doc.png")
resim = cv2.imread(resim_yolu)

#gri
gri = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
print("resim:",resim.shape)
print("gri:",gri.shape)
# eşikleme ile ikileştirme
(T,ikili_resim) = cv2.threshold(gri,60,255,cv2.THRESH_BINARY)#60 değerinin altındaki değerler siyah üstü beyaz
(Ti,ikili_resim_ters) =cv2.threshold(gri,60,255,cv2.THRESH_BINARY_INV)##60 değerinin altındaki değerler beyaz üstü siyah
cv2.imshow("orijinal resim",resim)
cv2.imshow("gri resim",gri)
cv2.imshow("ikili resim",ikili_resim)
cv2.imshow("ikili resim ters",ikili_resim_ters)
cv2.waitKey()

