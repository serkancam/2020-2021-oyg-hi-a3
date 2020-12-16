# %%sınıf tanımlama
#eğer bir fonskiyon sınıf içinde tanımlı ise
# aartık o bir method tur
class IlkSinif:
    def __init__(self,ad):#(constructor) yapıcı method denir
        print("nesne oluştu.",ad)

o1 = IlkSinif("hasan")#görülmeyen bir yapıcı var
o2 = IlkSinif("ali")

# print(type(o1),id(o1))
# print(type(o2),id(o2))
# %% insan sınıfı

class Insan:
    def __init__(self,ad,kl,by):#yapıcı method
        self.isim=ad
        self.kilo=kl
        self.boy=by
        print(self.isim,self.kilo,self.boy)
    def yemek_ye(self,miktar):
        self.kilo+=miktar
    def zayifla(self,kl:int):
        self.kilo-=kl
    def bkiHesapla(self):
        bki = self.kilo/(self.boy**2)
        return bki
        

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
# public neneye açık
# private sadece sınıf içerisinden -->
# --> kod ile erişilenilir
class Hayvan:
    def __init__(self,ad):
        self.isim=ad#public
        self.__agirlik=10.0#private özel oldu
        self.renk=""#public
    def setAgirlik(self,kilo):
        if kilo>0:
            self.__agirlik=kilo
    def getAgirlik(self):
        return self.__agirlik
h1=Hayvan("kedi")
# h1.agirlik=-10
# print(h1.agirlik)

print(h1.isim)
# print(h1.__agirlik)
h1.setAgirlik(0.1)
print(h1.getAgirlik())


# %%
