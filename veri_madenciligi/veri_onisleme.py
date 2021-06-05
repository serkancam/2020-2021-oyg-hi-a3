#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% dosyayı içe ataralım
veri = pd.read_csv("kalp_rahatsizligi.csv")
veri.head()
print(veri.info())
print(veri.columns)
# %% sütu isimlerinini değiştirilmesi
veri.rename(columns={"gogus_agrisi_tipi":"gat"},inplace=True)
#%%
print(veri.info())
# %%
veri.rename(columns={
  "hareketsiz_kan_basinci":"hkb",
  "serum_kolestrol":"sk",
  "aclik_kan_sekeri":"aks",
  "elektrokardiyografi":"ekg",
  "en_yuksek_kalp_hizi":"eykh",
  "anjin_bagli_egsersiz":"abe",
  "st_depresyonu":"std",
  "st_egimi":"ste",
  "buyuk_damarlar":"bd"},inplace=True)
veri.info()

# %% yaş ve talasemi sütunlarının yok edilecerek yeni veri oluşturmak
veri2=veri.drop(["yas","talasemi"],axis=1)
print(veri2.info())
print(veri.info())

# %% satırları yok etmek, bd ve talasemi sütunlarında eksik olan verilerin silinmesi
veri3=veri.dropna(axis=0)
print(veri3.info())

# %% kayıp verilere yeni değerler atamak, büyük damar bd sütunundaki eksik verileri en çok geçen değer ile dğiştirelim
print(veri.info())
from sklearn.impute import SimpleImputer

bds=veri["bd"].values.reshape(-1,1)
imputer=SimpleImputer(missing_values=np.nan,strategy="most_frequent")
#print(bds)
bds_yeni=imputer.fit_transform(bds)
# print(bds_yeni)
print(veri.info())
veri["bd"]=bds_yeni
print(veri.info())

# %%
