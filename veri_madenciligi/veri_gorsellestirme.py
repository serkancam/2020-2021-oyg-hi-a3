#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

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

sns.histplot(data=veri,x="serum_kolestrol",bins=10,element="step",palette="Dark2")
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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
veri = pd.read_csv("kalp_rahatsizligi.csv")
# %% serum kolstrol değerinin kutun grafiği
veri.info()
veri.describe()
sns.boxplot(data=veri,y="serum_kolestrol")
plt.show()
# %%

sns.boxplot(data=veri, y="serum_kolestrol",x="cinsiyet")
plt.show()

# %% en yüksek kalp hizi değerinin kutu grafiğini hemen ardındanda en yüsek kalp hızının cinsiyete göre kutu grafiğini çizdiriniz
sns.boxplot(data=veri, y="en_yuksek_kalp_hizi",)
plt.show()
sns.boxplot(data=veri, y="en_yuksek_kalp_hizi",x="cinsiyet")
plt.show()
# %%
sns.boxplot(data=veri, y="en_yuksek_kalp_hizi",x="kalp_rahatsizligi")
plt.show()

# %%
sns.boxplot(data=veri,y="serum_kolestrol")
plt.show()
# %% alt sınır/üst sınır
veri.describe()
k_q1=veri["serum_kolestrol"].describe()[4]
k_q3=veri["serum_kolestrol"].describe()[6]
k_iqr=k_q3-k_q1
k_as=k_q1-1.5*k_iqr
k_us=k_q3+1.5*k_iqr
print(f"serumm kolestrol alt sınırı={k_as}")
print(f"serumm kolestrol üst sınırı={k_us}")

ayrik1=veri[veri["serum_kolestrol"]>k_us]
ayrik2=veri[(veri["serum_kolestrol"]>k_us) | (veri["serum_kolestrol"]<k_as)]
ayrik2
# %% hareketsiz kan basıncı için aykırı verilerin temizlendiği yeni veri seti oluşturun
q1 = veri["hareketsiz_kan_basinci"].describe()[4]
q3 = veri["hareketsiz_kan_basinci"].describe()[6]
iqr=q3-q1
alt=q1-1.5*iqr
ust=q3+1.5*iqr
print(f"istirahat kan basınıcı alt sınır={alt}")
print(f"istirahat kan basınıcı üst sınır={ust}")
temiz=veri[(veri["hareketsiz_kan_basinci"]>=alt)&(veri["hareketsiz_kan_basinci"]<=ust)]
sns.boxplot(data=temiz,y="hareketsiz_kan_basinci")
plt.show()
sns.boxplot(data=veri,y="hareketsiz_kan_basinci")
plt.show()
# %%
veri.corr()
sns.heatmap(data=veri.corr(),annot=True,linewidths=0.5,fmt="0.1F")
plt.show()

# %%
