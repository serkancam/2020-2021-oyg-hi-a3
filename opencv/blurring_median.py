import cv2
import os
import numpy as np

# kaynak dizin: projemizin çalıştığı dosya yolunun adresi.--> cd (current directory)
cd = os.getcwd()
# resim yolu : kodumuzun içinde kullancağamız resmin yolu --> image_path
image_path = os.path.join(cd,"opencv","images","chp2","salt-pepper.jpg")
# resim :  kodumuzun içinde kullanacağımız resmi temsil eden değişken
# bu değişken türü numpy tipinde ve 3 boyutlu bir dizi.--> image
image = cv2.imread(image_path)
cv2.imshow("orijinal resim",image)
# 3*3 lük yani 9 piksellik
# ***
# ***
# ***
# 3*3 lük piksellere bölünmüş resmin yumuşatılmış haline--> blurm3
blurm3 = cv2.medianBlur(image,3)
cv2.imshow("blurm3",blurm3)
# 5*5 lük piksellere bölünmüş resmin yumuşatılmış haline--> blurm5
blurm5 = cv2.medianBlur(image,5)
cv2.imshow("blurm5",blurm5)
# 7*7 lük piksellere bölünmüş resmin yumuşatılmış haline--> blurm7
blurm7 = cv2.medianBlur(image,7)
cv2.imshow("blurm7",blurm7)
cv2.waitKey(0)
# cv2.destroyAllWindows()