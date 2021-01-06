#%%
def oztoplam(liste):
    toplam=0
    for i in liste:
        if type(i)==int or type(i)==float:
            toplam+=i
        if type(i)==list or type(i)==tuple or type(i)==set:
            toplam+=oztoplam(i)
        if type(i)==dict:
            toplam+=oztoplam(i.values())

    return toplam

if __name__=="__main__":
    t1 = ["12","ali",1,2.0,10] 
    t2 = (1,2,(10,3,{3,6,3}))
    t3 = {"a":1,"b":[t1,t2]}
    t4 = (1,2,[3,(4,5,{7,8}),{"a":12,"b":[3,8,[12]]}])
    t5 = [[9,8],[10,21]]
    print(oztoplam(t1))#13.0
    print(oztoplam(t2))#25
    print(oztoplam(t3))#39.0
    print(oztoplam(t4))#65
    print(oztoplam(t5))
# %%
