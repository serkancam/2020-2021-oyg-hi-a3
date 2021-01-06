#%%
# numpy da oluşan yapılara dizi diyeceğiz(ndarray)
# n dimension array---> n boyutlu dizi
# diziler düzgün şekilli olmalı ve dizideki her elemanın tipi aynı olmalı
# int float str den daha geniş bir tio havuzu var
# int8 int16 int32 int64 float8 float16 float64 float128
# uint8 uint16....
import numpy as np
a = [1,2,3]

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
nd1=np.array([3,8,32])
print("elemen sayısı:\t",nd1.size)
print("dizi şekli:\t",nd1.shape)
print("eleman tipi:\t",nd1.dtype)
print("dizi boyutu:\t",nd1.ndim)

# %%
nd2 = np.array([[3,8,7],[5,4,1]],dtype=np.uint8)
print("elemen sayısı:\t",nd2.size)
print("dizi şekli:\t",nd2.shape)
print("eleman tipi:\t",nd2.dtype)
print("dizi boyutu:\t",nd2.ndim)
# %%
