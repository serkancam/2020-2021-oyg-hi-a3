# %% fonksiyonlar iş yapış şekillerine göre

# bir iş yapanlar
print("merhaba")

# sonuç döndürenler
a = input("sayı gir:")
print(input("giriş:"))
# %% ilk fonsiyon

# fonksiyon 2 kısımdan oluşur.
# tanım(definition)
# çağırma-gerçekleme(call-invoke)


def ilkFonksiyon():
    print("merhaba dünya")



ilkFonksiyon()
# %% argüman veya parametre


def selam_ver(isim):
    print("merhaba", isim)


selam_ver("hasan")
ad = "pınar"
selam_ver(ad)

# %% birden fazla argüman kullanımı


def dortgen_alani(kk, uk):
    print("alan=", kk*uk)


dortgen_alani(20, 30)
# %% örnek
# ad ,soyad ve yas argumanlarını
# alıp ekrana merhaba ad soyad yaş= yaş
# merhaba hasan can 13


def selam_ver2(ad, soyad, yas):
    print("merhaba", ad, soyad, "yaş=", yas)


selam_ver2("hasan", "can", 13)

# bu argüman kullanımına konumsal yol
# (positional way)
# %% anahtar kelime kullanımı (keywords way)


def selam_ver3(ad, soyad, yas):
    print("merhaba", ad, soyad, "yaş=", yas)


selam_ver3(yas=13, ad="hasan", soyad="can")

# %% karışık(mixing) paramtere kullanımı


def hesapla(a, b, c, d):
    sonuc = a+b*c/d
    print("sonuç=", sonuc, "|", a, b, c, d)


hesapla(1, 2, 10,5)  # konuma bağlı
hesapla(a=10, d=8, b=20, c=3)  # anahtar kelime yolu
hesapla(1, 5, d=3, c=10)  # karışık kullanım
# karışık kullanımda
# ilk önce konuma bağlı argümanlar yazılır en son
# anahtar kelimeye bağlı argümanlar yazılır.
# hesapla(c=8,1,2,d=5)#hata
# hesapla(1,2,d=5,b=8) # hata
print("merhaba", "nasılsın?", sep="½", end="@")
print()
print("merhaba", "nasılsın?", end="½", sep="@")

# %% geriye değer(ler) döndürme return


def daire_alani(r,pi=3):
    alan = pi*r*r
    return alan  # return 3*r*r


print("alan=", daire_alani(5,3.14))

# %% bir listeyi parametre olarak alıp liste
# elemanlarının toplamını bulsun ve
# o sonucu gerei döndürsün


def liste_toplami(lst:list):
    t = 0
    for eleman in lst:
        t += eleman  # t=t+eleman
    return t
    print("selam")


h = [1, 2, 30, 52]
sonuc = liste_toplami(h)
print(sonuc)
# %% artık yıl mı?

# 00 ile biten yıllarda 400'e kalansız bölünenler
# bunun dışındaki yıllarda ise 4'e kalansız bölünenler
# artık yıldır


def artikYilMi(yil: int):  # isLeapYear
    if yil%100==0:
        if yil%400==0:
            return True
        else:
            return False
    else:
        if yil%4==0:
            return True
        else:
            return False

    


print(artikYilMi(2000))  # True
print(artikYilMi(1700))  # False
print(artikYilMi(2004))  # True
print(artikYilMi(2001))  # False
# %% asallık testi
def isPrime(sayi):
    a=1
    for bolen in range(2,sayi):
        #print(bolen)
        if sayi%bolen==0:
            return False,bolen
    return True


print("dönüş",isPrime(21218747))
print(a)
# %% varsayılan değer deafault
def hacim_hesapla(a,b=2,c=3):
    return a*b*c

print(hacim_hesapla(3,5,8))
print(hacim_hesapla(5))
print(hacim_hesapla(5,10))
# fonksiyon tanımındasoldan sağa varsayılan değer ,
# verilen argümandan sonra her argümana
# varsayılan değer verilmelidir.
# %% Değişkenlerin geçerlilik alanı 
#  global anahtar kelimesi

def bisey():
    x=10
    print(x)

bisey()
print(x)


# %%
#global değişken
x=10 

def bisey2():
    print(x)
    #x=10 bu hatadır
    
    

bisey2()
print(x)
# %%

x=10
print(id(x))
def bisey3():

    x=20
    print(x,id(x))

bisey3()
print(x)

# %%



def bisey4():
    global x
    x=20
    print(x,id(x))

bisey4()
print(x,id(x))

# %% üçgen olmakuralı + heron formülü
# elinizde 3 sayı var 
# ve bu 3 sayıyı kenar uzunluğu olarak alırsak
# acabna bu kenar uzunluğu 
# ile üçgen oluşturabilir miyiz?

def ucgenMi(a,b,c):
    return a+b>c and a+c>b and b+c>a

def ucgenAlani(x,y,z):
    if ucgenMi(x,y,z):
        s=(x+y+z)/2
        alan=(s*(s-x)*(s-y)*(s-z))**.5
        return alan
    else:
        return "üçgen değil"


print(ucgenAlani(1,3,4))
print(ucgenAlani(8,3,4))
print(ucgenAlani(7,6,4))
print(ucgenAlani(3,4,5))

# %% 3 sayıdan en küçük 2 tanesi

def enKucuk2si(s1,s2,s3):
    if s1>s2>s3:
        print(s2,s3)
    elif s2>s1>s3:
        print(s1,s3)
    else:
        print(s1,s2)

enKucuk2si(5,5,5)
enKucuk2si(5,10,10)

# %% problemler 3 farklı yolla çözülür.
# 1. yöntem formül 
# örnek olarak
# hız=yol/zaman bir zamanda gidilen yolu zaman değerine bölersek hız bulunur
# 1-1000 arasındaki sayıların toplamı 
def arasindakiToplam1(son:int):
    toplam=son*(son+1)/2
    return toplam
def arasindakiToplam2(son:int):
    toplam=0
    for i in range(1,son+1):
        toplam+=i
    return toplam
sonSayi=int(input("sayı gir:"))

print(arasindakiToplam1(sonSayi))
print(arasindakiToplam2(sonSayi))


# %% 2. yönetem İteratif(döngüsel) yöntem
# örnek fiboancci serisi
def fib1(adim):
    if adim<1:
        return None 
    if adim<3:
        return 1
    f1=1
    f2=1
    for _ in range(3,adim+1):
        f1,f2 = f2, f1+f2
    return f2

print(fib1(2))
print(fib1(3))
print(fib1(4))
print(fib1(7))
print(fib1(1000))

# %% 3. yol özyinelemeli(recursive-recursion)
def fib2(adim):
    if adim<1:
        return None
    if adim<3:
        return 1 
    return fib2(adim-1)+fib2(adim-2)
print(fib2(2))
print(fib2(3))
print(fib2(4))
print(fib2(33))
print(fib2(39))

# %%
