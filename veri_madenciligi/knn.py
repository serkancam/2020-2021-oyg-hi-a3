#%% kütüphaneler
import pandas as pd
import numpy as np

# %%
veri = pd.read_csv("kalp_rahatsizligi.csv")
# %%
veri.rename(columns={
    "gogus_agrisi_tipi":"gat",
    "hareketsiz_kan_basinci":"hkb",
    "serum_kolestrol":"sk",
    "aclik_kan_sekeri":"aks",
    "elektrokardiyografi":"ekg",
    "en_yuksek_kalp_hizi":"eykh",
    "anjin_bagli_egsersiz":"abe",
    "st_depresyonu":"st_d",
    "st_egimi":"st_e",
    "buyuk_damarlar":"bds"},inplace=True)
# %% 1- eksik verilerin giderilmesi
from sklearn.impute import SimpleImputer
imp=SimpleImputer(missing_values=np.nan,strategy="most_frequent")
bds=veri["bds"].values.reshape(-1,1)
tal=veri["talasemi"].values.reshape(-1,1)
veri["bds"]=imp.fit_transform(bds)
veri["talasemi"]=imp.fit_transform(tal)


# %% 3 kategorik verileri sayısallaştırmak
#  kategorik verilerin etiketlenmesi
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
veri["cinsiyet"]=le.fit_transform(veri["cinsiyet"])
veri["gat"]=le.fit_transform(veri["gat"])
veri["ekg"]=le.fit_transform(veri["ekg"])
veri["st_e"]=le.fit_transform(veri["st_e"])
veri["talasemi"]=le.fit_transform(veri["talasemi"])

#%%4-5 sayısal verileri 0-1 arasına normalize etmek
from sklearn.preprocessing import minmax_scale
X=veri.iloc[:,0:-1].values
Y=veri.iloc[:,13].values
# %% burada sayısal veri olan sütunlar 0-1 arasına normalize edildi.
X[:,[0,3,4,7,9,11]]=minmax_scale(X[:,[0,3,4,7,9,11]],
feature_range=(0,1))
# %% 6- 303 verimizin bir kısmını eğitim için bir kısmınıda test iiçin ayıralım
 #x_train,y_train---x_test,y_test///%80 eğitimiçin %20 test için
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

# %% 7- oluşan sistemi eğitmek(k en yakın komşu-k-neares neighbors) 
# ve yeni modelin bize yüzde kaç doğrulukla cevap verdiğini test etmek.
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

# %% test edelim 
tahmin=knn.predict(x_test)
for i in range(len(tahmin)):
    print(f"gerçek durum:{y_test[i]}--tamin edilen:{tahmin[i]}")

# %% öğrenme skoru
ogrenme_skoru=knn.score(x_test,y_test)
print(f"skor={ogrenme_skoru}")

# %%
