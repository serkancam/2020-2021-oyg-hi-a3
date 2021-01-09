def enkb(liste):
    enkucuk=liste[0]
    enkucukyeri = 0
    for i in range(1,len(liste)):
        if liste[i]<enkucuk:
            enkucuk=liste[i]
            enkucukyeri=i
    return  enkucukyeri

def sec_sirala(liste):
    sl=[]#listenin sıralanmış hali
    for _ in range(len(liste)):
        ekey = enkb(liste)
        siradaki = liste.pop(ekey)
        sl.append(siradaki)
    return sl

def hizli_siralama(listem:list):
    if len(listem)<2:
        return listem
    else:
        pivot = listem[0]
        sol = [ i for i in listem[1:] if i<=pivot]
        sag = [i for i in listem[1:] if i>pivot]

        return hizli_siralama(sol)+ [pivot] + hizli_siralama(sag)



import random
from datetime import datetime
listem = [random.randint(1,1000_000_000) for _ in range(2000_000)]
print(len(listem))

ssl = listem.copy()
hsl = listem.copy()

# seçerek sıralama
# ssBasla = datetime.now()
# sirali = sec_sirala(ssl)
# ssBitis = datetime.now()
# print("seçerek sırlama işlem zamanı:",ssBitis-ssBasla)

# huzlı sıralama
# hsBasla= datetime.now()
# sirali = hizli_siralama(hsl)
# hsBitis =datetime.now()

# print("hızlı sırlama zamanı:",hsBitis-hsBasla)

# python dahili liste sıralaması sıralama
psBasla= datetime.now()
sirali = listem.sort()
psBitis =datetime.now()
print("hızlı sırlama zamanı:",psBitis-psBasla)