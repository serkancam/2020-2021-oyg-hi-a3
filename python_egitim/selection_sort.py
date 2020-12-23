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

listem=[16,9,98,25,30,50,12,20,10,55]
print("sırasız:\n",listem)
sirali = sec_sirala(listem)
print("sıralı:\n",sirali)