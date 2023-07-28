"""Görev 8:
Aşağıda 2 adetset verilmiştir. 
Sizden istenilen eğer 1.  küme 2. kümeyi kapsiyorise ortak elemanlarını eğer kapsamıyorise
2. kümenin 1. kümeden farkını yazdıracak fonksiyon u tanımlamanız beklenmektedir

"""
kume1=set(["data","python"])
kume2=set(["data","function","qcut","lambda","python","miuul"])

def kapsama(kume1,kume2):
    A=list(kume2)
    for kume in kume1:
        if kume in kume2:
            del A[A.index(kume)]
    return A
print(kapsama(kume1,kume2))
        

           
            
