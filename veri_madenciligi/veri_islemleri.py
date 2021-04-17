#%%
import numpy as np 
import pandas as pd 
from  scipy import stats

# %%
veri = pd.read_csv("kalp_rahatsizligi.csv")
print(veri)
# %% kişlerin yaş ortalaması
yas_ort=veri["yas"].mean()
yas_ortanca=veri["yas"].median()
print("yaş ortalaması=",yas_ort)
print("yaş ortancası=",yas_ortanca)

# %%
veri.info()
# %%
ser_ort=veri.serum_kolestrol.mean()
ser_ortanca=veri.serum_kolestrol.median()
print("kolestrol ortalması=",ser_ort)
print("kolestrol ortancası=",ser_ortanca)
# %% en çok tekrar eden yas
yas_mod=stats.mode(veri["yas"])
print(yas_mod)

# %% yaş değerinin standart sapması
yas_std = veri.yas.std()
yas_var = veri.yas.var()
yas_ort=veri["yas"].mean()
yas_ortanca=veri["yas"].median()
print("yaş ortalaması=",yas_ort)
print("yaş ortancası=",yas_ortanca)
print("yaş std=",yas_std)
print("yaş varyans=",yas_var)
# yş değerlerinin yaklaşık %68i 45-63
# %% serum kolestrrol değeri %68 kişi de hangi değerler arasındadır
serum_ort = veri["serum_kolestrol"].mean()
serum_std = veri["serum_kolestrol"].std()
print("kolstrol ortalaması=",serum_ort)
print("kolstrol stdandart sapması=",serum_std)
print("Veilerin yaklaşık %68'inin serum kolestrol değeri",serum_ort-serum_std,"ile",serum_ort+serum_std,"değerleri arasındaıdr")

# %% yaş ve kolestrol değerlkerinin aralığı
yas_min=veri["yas"].min()
yas_max=veri["yas"].max()
print("yaş aralığı=",yas_max-yas_min)
kol_min=veri["serum_kolestrol"].min()
kol_max=veri["serum_kolestrol"].max()
print("kolestrol aralığı",kol_max-kol_min)



# %%
