# %%sınıf tanımlama
#eğer bir fonskiyon sınıf içinde tanımlı ise
# artık o bir method tur
class IlkSinif:
    def __init__(self,ad):#(constructor) yapıcı method denir
        print("nesne oluştu.",ad)

o1 = IlkSinif("hasan")#görülmeyen bir yapıcı var
o2 = IlkSinif("ali")
print(dir(IlkSinif))
# print(type(o1),id(o1))
# print(type(o2),id(o2))
# %% insan sınıfı

class Insan:
    def __init__(self,ad,kl,by):#yapıcı method
        self.isim=ad
        self.kilo=kl
        self.boy=by
        # print(self.isim,self.kilo,self.boy)
    def yemek_ye(self,miktar):
        self.kilo+=miktar
    def zayifla(self,kl:int):
        self.kilo-=kl
    def bkiHesapla(self):
        bki = self.kilo/(self.boy**2)
        return bki


jale = Insan(ad="jale",by=1.70,kl=56)  
hasan = Insan("hasan",79,1.85)

# print(hasan.isim)
# hasan.isim="mustafa"
# hasan.kilo=78
# print(hasan.isim)
# print(hasan.kilo)
# print(hasan.bkiHesapla())
i1=Insan(kl=35,by=1.65,ad="irem")
i2=Insan("yusuf",51,1.55)
i3=Insan("serkan",82,1.74)
print(i3.isim)
print(i2.boy)
print(i3.kilo)
i3.yemek_ye(2)
print(i3.kilo)
i3.zayifla(5)
print(i3.kilo)
print(i1.isim," bki değeri:",i1.bkiHesapla())
print(i2.isim," bki değeri:",i2.bkiHesapla())
print(i3.isim," bki değeri:",i3.bkiHesapla())

# %%
i3.boy=-1.0
print(i3.boy)
# %% Bilgi gizleme/kapsülleme
# public nesneye açık
# private sadece sınıf içerisinden -->
# --> kod ile erişilenilir
class Hayvan:
    def __init__(self,ad):#yapıcı
        self.isim=ad#public
        self.__agirlik=10.0#private özel oldu
        self.renk="renksiz"#public
    def setAgirlik(self,kilo):#bu nesnenin ilgili özelliğini değiştirir
        if kilo>0:
            self.__agirlik=kilo
    def getAgirlik(self):
        return self.__agirlik
h1=Hayvan("kedi")
# h1.agirlik=-10
# h1.agirlik=-10
print(h1.isim)
h1.setAgirlik(3)
print(h1.getAgirlik())

# print(h1.isim)
# print(h1.__agirlik)
# h1.setAgirlik(0.1)
# print(h1.getAgirlik())


# %%
import random
class Hayvan:
    def __init__(self,ad):#yapıcı
        self.isim=ad#public
        self.__agirlik=random.randint(1,30)#private özel oldu
        self.renk="renksiz"#public
    def setAgirlik(self,kilo):#bu nesnenin ilgili özelliğini değiştirir
        if kilo>0:
            self.__agirlik=kilo
    def getAgirlik(self):
        return self.__agirlik
        
hayvanlar=[]

for i in range(100):
    hayvan = Hayvan("hayvan"+str(i))
    hayvanlar.append(hayvan)


print(hayvanlar[3].isim)
print(hayvanlar[3].getAgirlik())
print(hayvanlar[90].isim)
print(hayvanlar[90].getAgirlik())
# %%
# hayali araba

# arabanın özellikler
# marka, model yılı, renk, kaç km de
# arabanın davranışları
# git(km) bu değer sürekli kaçkm de değişkenine eklensin
#arabayı_boya(renk)
#model yılı private olsun 

class Araba:
    def __init__(self,marka:str,model_yili:int,renk:str,kacKm:int):
        self.marka=marka
        self.model_yili=model_yili
        self.renk=renk
        self.kacKm=kacKm
    def git(self,km:float):
        self.kacKm+=km
    def arabayi_boya(self,renk:str):
        self.renk=renk
    def __str__(self):
        return self.marka+"-"+str(self.model_yili)


a1 = Araba("fiat",2018,"gri",56000)
a1.git(7.8)

print(a1.kacKm)
print(a1.renk)
a1.arabayi_boya("füme")
print(a1.renk)


# %%
print(dir(Araba))
# %%
print(a1)

# %%  miras(inheritance)
# miras olarak ata sınıftan sadece public olanlar 
# miras olarak çocuk sınıfa geçer
class Hayvan:
    def __init__(self,ad):
        self.__ad = ad#private
        self.yas=10 #public
        print("Hayavan sınıfı yapıcı çalıştı.",self.__ad)
    def ses_cikar(self):
        print("hayvanı ses çıkardı.")

class Kedi(Hayvan):
    #method ezme(method override)
    def __init__(self,ad):
        self.__ad=ad
        self.__yas=20
        print("Kedi Sınıfı yapıcısı çalıştır",self.__ad)
    def ses_cikar(self):#method ezme(method override)
        print("miyavvvv...")

class Kopek(Hayvan):
    def ses_cikar(self):#method ezme(method override)
        print("hav hav")

class Kus(Hayvan):
    pass

h1 = Hayvan("hayvan1")
kd1 = Kedi("kedi 1 ")
kp1 = Kopek("köpek 1")
ks1 = Kus("maşuk")
h1.ses_cikar()
kd1.ses_cikar()
kp1.ses_cikar()
ks1.ses_cikar()

print(h1.yas,kp1.yas,kd1.yas,ks1.yas)
#%%

# %%
