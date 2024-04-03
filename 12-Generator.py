# Diyelim ki elimizdeki bir listenin elemanlarıın karesini almak istiyoruz:

def square(l):
    res = []

    for e in l:
        res.append(e*e)
    return res

l = [1, 2, 3]
print(square(l))

# Peki bu değerleri bir anda hesaplasın da kullanıcı sordukça üretip döndürse
# Bu işlemi generator mantığı ile yapabiiriz.

def square_generator(l):
    for e in l:
        yield e*e
l = [1, 2, 3]
g = square_generator(l)
print(next(g))
print(next(g))
print(next(g))
# Fonksiyonlar returnden sonrakini döndürüp kapanıp gidiyorlar. Generatorler
# yielden sonrakini döndürüp kapanıp gitmiyor sıradaki sıradaki diye döndürecek
# bir şey kalmayana kadar devam ediyorlar. 
# Generator'ler bütün cevabı hafızada tutmazlar, biz sordukça değer döndürürler.
# Generatorlar iterator'dur. next ile sonraki değerlerine erişebiliriz.


     