#Bir listeyi düzleştiren (flatten) fonksiyon yazın. 
# Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. 

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
lnew = []
def flatten(n):
    for i in n: #Burada listenin elemanları teker teker döngüye sokuluyor. 
        if isinstance(i, list): #elemanların list olup olmamasını durumu karşılaştırılıyor.  
            flatten(i) #İf bloğunun sonucunda elemanlar list halinde ise tekrar flatten fonksiyonuna sokuldu. 
        else: 
            lnew.append(i) #eleman list halinde değilse listeye eklendi. 

flatten(l) #Oluşturulmuş olan flatten fonsiyonumuzun içinde listemizi çalıştırdık.
print(lnew) 
