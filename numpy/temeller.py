#%%
# numpy da oluşan yapılara dizi diyeceğiz(ndarray)
# n dimension array---> n boyutlu dizi
# diziler düzgün şekilli olmalı ve dizideki her elemanın tipi aynı olmalı
# int float str den daha geniş bir tip havuzu var
# int8 int16 int32 int64 float8 float16 float64 float128
# uint8 uint16....
import numpy as np
a = [1,2,3,4]

nd0 = np.array(a,dtype=np.uint8)

print(type(nd0))
print(nd0.size)
print(nd0.shape)
print(nd0.dtype)
print(nd0.ndim)

# %% ilk boyut sklaer yani 0-D
nd0=np.array(3)
print("elemen sayısı:\t",nd0.size)
print("dizi şekli:\t",nd0.shape)
print("eleman tipi:\t",nd0.dtype)
print("dizi boyutu:\t",nd0.ndim)


# %% 1-D 
nd1=np.array([3,8,32],dtype=np.uint8)
print("elemen sayısı:\t",nd1.size)
print("dizi şekli:\t",nd1.shape)
print("eleman tipi:\t",nd1.dtype)
print("dizi boyutu:\t",nd1.ndim)

# %% 2 boyut
nd2 = np.array([[3,8,7],[5,4,1]],dtype=np.uint8)
print("elemen sayısı:\t",nd2.size)
print("dizi şekli:\t",nd2.shape)
print("eleman tipi:\t",nd2.dtype)
print("dizi boyutu:\t",nd2.ndim)
# %%n 3 boyut
import numpy as np
listem = [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
nd3 = np.array(listem)
print("elemen sayısı:\t",nd3.size)
print("dizi şekli:\t",nd3.shape)
print("eleman tipi:\t",nd3.dtype)
print("dizi boyutu:\t",nd3.ndim)
# %% zeros() ones() full()
import numpy as np

sifirler = np.zeros((100,50),dtype=np.uint8)
print(sifirler)
print(sifirler.ndim)
print(sifirler.shape)



# %%
import numpy as np

birler = np.ones((100,50),dtype=np.uint8)
print(birler)
print(birler.ndim)
print(birler.shape)
# %%
import numpy as np

birler = np.full((100,50),200,dtype=np.uint8)
print(birler)
print(birler.ndim)
print(birler.shape)
# %%
import numpy as np

birler = np.full((100,50),"serkan")
print(birler)
print(birler.ndim)
print(birler.shape)
# %% arange komutu

import numpy as np

sd = np.arange(9)
print(sd)
sd1 = np.arange(9,16)
print(sd1)
sd2 = np.arange(0,82,9)
print(sd2)

sd2.shape = (2,5)
print(sd2)



# %% randint

import numpy as np 
import cv2

rd = np.random.randint(0,255,(200,200),dtype=np.uint8)
rd.shape = (400,100)
print(rd)

cv2.imshow("resim",rd)

cv2.waitKey(0)



# %% kesme işlemleri

import numpy as np

test = np.arange(1,21)
test.shape=(4,5)
print(test)
print(30*"*")
print(test[0])#ilk satır
print(30*"*")
print(test[-1])#son satr
print(30*"*")
print(test[1:3])#orta 2 satur
print(30*"*")

print(test[2:])#son iki satır
print(30*"*")
print(test[:,0])
print(30*"*")
print(test[:,-1])
print(30*"*")
print(test[1:3,1:3])



# %%
# %% skaler işlemler
import numpy as np

a = np.array([[1, 2],[3, 4]])
b = np.array([[40, 30],[20, 10]])

print("skaler işlemler:")
print("a+1:",a+1,end="\n\n")
print("a*2:",a*2,end="\n\n")
print("b/3:",b/3,end="\n\n")
print("b-2:",b-2,end="\n\n")
print("np.sgrt(a):",np.sqrt(a),end="\n\n")
print("a*a:",a*a,end="\n\n")
print("a+b:",a+b,end="\n\n")# ayı şekle sahip olanlar da 4 işlem yapılabilir.
# %%
