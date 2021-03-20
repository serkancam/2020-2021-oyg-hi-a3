import cv2 
import os
import numpy as np

canvas_r = np.zeros((200,200,3),dtype=np.uint8)
canvas_c = canvas_r.copy()

#rectangle için değişkenler tanımladık
start = (10,10)
end = (100,100)
color_r = (0,0,255)
color_c = (255,0,0)
thickness =4 #eğer thickness değer -1 olursa içi dolu bir çizim yapır
#rectangle çizdirdik
cv2.rectangle(canvas_r,start,end,color_r,thickness)
#circle çizdirelim
cv2.circle(canvas_c,(100,100),50,color_c,-1)
# bu imajı gösterdik
cv2.imshow("rectangle",canvas_r)
cv2.imshow("circle",canvas_c)
# imajı kaydetmnek için yol(path) oluşturduk.
cd  = os.getcwd()
r_path = os.path.join(cd,"opencv","images","chp1","rect.jpg")
# imajı diske belirlediğimiz yola kaydettik.
cv2.imwrite(r_path,canvas_r)
#######################################
# imajı kaydetmnek için yol(path) oluşturduk.
cd  = os.getcwd()
c_path = os.path.join(cd,"opencv","images","chp1","circle.jpg")
# imajı diske belirlediğimiz yola kaydettik.
cv2.imwrite(c_path,canvas_c)

cv2.waitKey(0)
