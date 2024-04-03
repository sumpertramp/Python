#Create a Class
#Fonksiyonlarda belirli fonksiyonaliteleri ifade eden kodları bir araya getirmeyi biliyoruz.
#Class mantığında hem fonksiyonalite hem de veriyi bir arada tutma yoluna bakacağız.
#Class'ın içerisindeki datalara attribute, fonksitonlara method diyeceğiz.
#Diyelim ki bir iş yeri çalışanlarını kodumuzda ifade etmek istiyoruz. Sanki bu class mantığı
#ile uyumlu. Her çalışanın farklı farklı özellijkleri (attribute)'ları ve yaptıkları şeyler
#(method)ları olacak
#Class yaratırken class kullanılır.
#Class'ın içerisinde method yaratırken, class'dan yaratılan objeyi methodlar ilk argüman
#olarak alırlar. İstediğimiz adı verebiliriz ama genellikle self diye geçer.

class Employee:
    pass

#Sınıftan obje oluşturduk
e = Employee() 

# e objesine a attribute'u ekleyelim
e.a = 4
print(e.a)

# Böyle tek tek oluşturmak yerine en başta class'ı oluştururken de attribute verebiliriz.
class Employee:
    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
    
    def fullname(self):
        print(f"{self.name} {self.last}")
    
#Class attributelerden objeler yaratmak için bir kalıptır.
#emp_1 adında Employee clasının bir objesini yaratıyoruz.
emp_1 = Employee("James", "Hughes", "32", 5000)
emp_2 = Employee("Charlie", "Brown", "22", 3000)

print(emp_1.name)

# Yukarıda yarattığımız bütün attributelar instance variable'dir. Her obje
# (class'dan yaratılan instance), kendine özel attribute'lara sahip (iki 
# kişinin adı aynı olabilir, ama hepsi için ayrı bir variable var ve hepsi
# kendi age attribute'unda tutuluyor.)

#Oluşturduğumuz methodları çağıralım:
print(emp_1.fullname())
print(emp_2.fullname())
