#Args 
#Args değişken sayılı parametre vermenin bir yoludur.
#List/Tuble objelerini unpack yapar ama dictionary objelerini yapmaz.

def sum(numbers):
    res = 0
    for e in numbers:
        res += e
    return res

#numbers = [1,2,3,4]
#print(sum(numbers))

numbers = [1,2]
print(sum(numbers))

#args'ın yapmış olduğu şey, başlangıçta list/tuble gibi bir obje varken 
#bunu tek tek elemanlarına ayırır.
#Yani yukarıdaki örnekte olduğu gibi numbers dizisi sürekli eleman sayısı
#değişen ve örneğin elemanlarına sürekli bir eklemenin yapıldığı data
#dizisi olduğunda yukarıdaki kod işimizi görmeyecektir.
#Böyle durumlarda *args kullanılır. Args'da tuple list gibi bir tipi unpack
#ederek çalışır.
 

def sum(*args):
    res = 0
    for e in args:
        res += e
    return res
print(sum(1, 2, 3, 4))

#Yukarıdaki örnekte *args = 1, 2, 3, 4 olduğunu varsaydı, yani argsın
#tek tek elemanlarına ayrılmış hali 1,2,3,4 ise orjinali unpack edilmemiş
#hali args = (1,2,3,4) olur.

def sum(*numbers):
    res = 0
    print(type(numbers))
    print(numbers)
    for e in numbers:
        res += e
    return res
sum(1,2,3,4)

#Yukarıdaki kodda args'ın tuble olarak tuttuğunu görmüş olduk.

def sum_2(*args):
    res = 0
    print(type(args))
    print(args)
    print(len(args))
    for e in args:
        for j in e:
            res +=j
    return res

sum_2([1,2], [3,8])


