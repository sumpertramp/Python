# Fonksiyona değişken sayıda keyword argument verebilmemizi sağlar.
# Kwarg'da veri dictionaty olarak saklanır.

def students(**kwargs):
    for v in kwargs.values():
        print(v)

#students(name = "Jake", student_number = "401")

def students(**students):
    print(students)
    for v in students:
        print(v)

students(name = "Jake", student_number = "401")

#Using Args and Kwargs Together
#Burada kullanım sırası önemlidir. İlk args, sonra kwargs

def weird(*args, **kwargs):
    res = 0
    for e in args:
        res += e
    
    for k, v in kwargs.items():
        print(k, ":", v)
    return res
print(weird(1,2,3, name = "Jake", student_number = 401))







