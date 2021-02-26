import cv2
import numpy as np
import os

cd = os.getcwd()
image_path = os.path.join(cd,"opencv","images","chp2","zebra.png")

image_original = cv2.imread(image_path)
# 1. yöntem resize
h,w,c=image_original.shape
aspect_ratio=w/h

h_yeni=int(h*0.1)
w_yeni=int(aspect_ratio*h_yeni)
image_y1 = cv2.resize(src=image_original,dsize=(w_yeni,h_yeni))
# 2. yöntem

image_y2 = cv2.resize(src=image_y1,dsize=None,fx=10.0,fy=10.0,interpolation=cv2.INTER_CUBIC)



cv2.imshow("orjinal resim",image_original)
cv2.imshow("1. yontem",image_y1)
cv2.imshow("2. yontem",image_y2)

cv2.waitKey(0)

# INTER_LINEAR: Bu aslında en yakın dört komşunun (2 × 2 = 4) belirlendiği ve bir sonraki pikselin değerini belirlemek için ağırlıklı ortalamasının hesaplandığı bir çift doğrusal enterpolasyondur. 

# INTER_NEAREST: Bu, o noktanın etrafındaki noktalarda (komşu) noktalarda o fonksiyonun değeri verildiğinde, bir boşluktaki bir olmayan nokta için bir fonksiyonun değerini tahmin etmek için en yakın komşu enterpolasyon yöntemini kullanır. Başka bir deyişle, bir pikselin değerini hesaplamak için, en yakın komşusunun enterpolasyon fonksiyonuna yaklaştığı kabul edilir. 

# INTER_CUBIC: Bu, piksel değerini hesaplamak için bikübik enterpolasyon algoritması kullanır. Çift doğrusal enterpolasyona benzer şekilde, bir sonraki pikselin değerini belirlemek için 4 × 4 = 16 en yakın komşuyu kullanır. Hız bir sorun olmadığında, bikübik enterpolasyon, çift doğrusal ile karşılaştırıldığında daha iyi yeniden boyutlandırılmış bir görüntü sağlar. 

# INTER_LANCZOS4: Bu, 8 × 8 en yakın komşu enterpolasyonunu kullanır. 

# INTER_AREA: Piksel değerinin hesaplanması, piksel alanı ilişkisi kullanılarak gerçekleştirilir (OpenCV resmi belgelerinde açıklandığı gibi). Bu algoritmayı hareli olmayan yeniden boyutlandırılmış bir görüntü oluşturmak için kullanıyoruz. Görüntü boyutu büyütüldüğünde, INTER_AREA INTER_NEAREST yöntemine benzer.