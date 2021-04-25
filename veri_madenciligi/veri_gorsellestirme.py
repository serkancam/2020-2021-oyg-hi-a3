#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%% verinin alınması
veri = pd.read_csv("kalp_rahatsizligi.csv")
veri.info()
veri.columns
# %% yaş histogramı grafiği
# sns.histplot(data=veri,x=veri["yas"],bins=10)
sns.histplot(data=veri,x="yas",bins=10)
plt.xlabel("Yaş")
plt.ylabel("adet")
plt.title("Yaş histogramı")
plt.show()


# %% yaş histyaogramı kadın erkek grupları
sns.histplot(data=veri,x="yas",bins=15,hue="cinsiyet",element="step",palette="winter")
plt.show()

# %% serum_kolestrol vberisinin gogus_agrisi_tipi verisine göre histogramını çizdiriniz.

sns.histplot(data=veri,x="serum_kolestrol",bins=15,hue="gogus_agrisi_tipi",element="step",palette="Dark2")
plt.show()

# %% saçılım(scatter) grafiği iki sayısal değişken arasındaki ilişkiyi gösteren grafik türü
#%% yaş ve en yüksek kalp hızı rasındaki saçılım grafiği
sns.scatterplot(data=veri,x="yas",y="en_yuksek_kalp_hizi")
plt.title("Yaş/En yüksek kalp hızı")
plt.show()

#%% yaş ve en yüksek kalp hızı rasındaki saçılım grafiği/cinsiyete göre
sns.scatterplot(data=veri,x="yas",y="en_yuksek_kalp_hizi",hue="cinsiyet")

plt.title("Yaş/En yüksek kalp hızı")
plt.show()

# %% yaş ile serum kolestrol değeri
sns.scatterplot(data=veri,x="yas",y="serum_kolestrol",hue="cinsiyet")

plt.title("Yaş/serum koelstrol.")
plt.show()

# %% yaş/en_yuksek_kalp_hizi regresyon eğrisi

sns.regplot(x="yas",y="en_yuksek_kalp_hizi",data=veri)
plt.show()

# %% çizgi grafiği(lineplot) iki değişken arasındaki ilişikiyi gösterir. 
sns.lineplot(data=veri,x="yas",y="hareketsiz_kan_basinci",hue='kalp_rahatsizligi')
plt.show()

# %% çubuk/sütun (bar) grafiği
# kategorik verilerin dağılımı hakkında (histograın kategoreik veri içn olanı)

# kadın erkek sayıları grafiği
sns.countplot(data=veri,x="cinsiyet")
plt.show()

# %% elektrokardiyografi değerlerinin kalp rahatsızlığına göre sayıları

sns.countplot(data=veri,x="elektrokardiyografi",hue="kalp_rahatsizligi")
plt.show()

# %% cinsiyete göre talasemi sayıları
sns.countplot(data=veri,x="talasemi",hue="cinsiyet")
plt.show()

# %% cisniyete göre talasemi sayılarının gğüs ağrısı tipine göre gruplandırılması
sns.catplot(data=veri,x="talasemi",hue="cinsiyet",col="gogus_agrisi_tipi",kind="count",height=4,aspect=0.7)
plt.show()

# %%
