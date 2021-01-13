import cv2
import os 
import numpy as np

# proje yolumuzu bulalım

cd = os.getcwd()
# marsrober.png resminin yolunu bulalım
image_path = os.path.join(cd,"opencv","images","chp1","marsrover.png")
# print("çalışılan dizin:",image_path)

# resmi okuyalım
image = cv2.imread(image_path)
print(type(image),image.shape)
shape = image.shape
h = shape[0]
w = shape[1]
print(f"resim boyutu: {w}x{h}")
#ilk piksel rengi
first_px_color = image[0,0]
print(first_px_color)
# ilk 200x100 pikseli yeşil yapalım
image[0:100,0:200]=first_px_color#(0,255,0)

# resim üstüne bir çizgi (line) çizelim
start = (100,70)
end = (350,380)
line_color = (0,255,0)
line_color2 = (255,0,0)
thickness = 4
cv2.line(image,start,end,line_color,thickness)
# resim üstüne bir dikdörtgen
cv2.rectangle(image,start,end,line_color2,thickness)
cv2.imshow("resim",image)

cv2.waitKey(0)