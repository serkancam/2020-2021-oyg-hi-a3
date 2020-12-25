def hizli_siralama(listem:list):
    if len(listem)<2:
        return listem
    else:
        pivot = listem[0]
        sol = [ i for i in listem[1:] if i<=pivot]
        sag = [i for i in listem[1:] if i>pivot]

        return hizli_siralama(sol)+ [pivot] + hizli_siralama(sag)


listem=[16,9,98,25,30,50,12,20,10,55]

sirali = hizli_siralama(listem)

print("sırasız:\n",listem)
print("sıralı:\n",sirali)

