# def topla(l:list):
#     toplam=0
#     for i in l:
#         if isinstance(i, list):
#             toplam+=topla(i)
#         if isinstance(i, int) or isinstance(i,float):
#             toplam+=i

#     return toplam


# test = [[15,[30,5]],1,2,3,20,30,[5,2,[20,30,[20,20,40,[30]]]],[30,30]]

# print(topla(test))

# # print( isinstance(3.0,int) )

# # + operatörü iki tarafıda sayı(int,float) ise aritmatek toplama yar
# a = 5
# b = 10
# print(a+b)
# # + operatörü iki tarafıda dize(str) ise bu değerleri birleştirir(contecanate)
# c="ali"
# d="veli"
# print(c+d)

# # + operatörü iki tarafıda liste(list) ise bu değerleri birleştirirek liste yapar
# pivot = 30
# sol =[3,8]
# sag=[100,110]
# print(sol+[pivot]+sag)
