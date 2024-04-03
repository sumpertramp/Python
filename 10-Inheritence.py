# Inheritance belirttiğimiz başka methot ve attribute'lara erişmemizi sağlar.
# Diyelim ki farklı tipte çalışanlar yaratmak istiyoruz, IT ve HR çalışanları olsun.

class Employee:
    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
        Employee.num_emp += 1
    
    def apply_raise(self):
        self.pay = self.pay * self.raise_percent
    
    # Hangi class'dan inherit etmek istediğimizi parantezin içine yazıyoruz.
    # İnherit ettiğimiz class a parent/super class, inherit edene de child/subclass deniyor.
    
emp_1 = Employee("James", "Hughes", "32", 5000)
emp_2 = Employee("Charlie", "Brown", "22", 3000)

class IT(Employee):
    pass

# IT'nin içine hiç bir şey yazmasak da Employee'nin özelliklerine erişimi var.
# IT'nin içerisinde bulamaz ise aradığını, inherit ettiği yere gidip bakacak.
# IT'nin içerisinde __init__ methodu yok, o yüzden gidip Employee class'ına bakacak.

it_1 = IT("James", "Hughes", "32", 5000)
print(it_1.__dict__)

#help(IT) # Class yapısına bakmak için

print(it_1.pay)
it_1.apply_raise()
print(it_1.pay)

# Diyelim ki IT'dekilerin yüzdelik maaş değişimini farklı bir değer olarak belirlemek istiyoruz

class IT(Employee):
    raise_percent = 1.2

it_1 = IT("James", "Hughes", "32", 5000)
print(it_1.pay)
it_1.apply_raise()
print(it_1.pay)

# Yukarıda Employee'nin raise_percent attribute'unu kullanmak yerine kendisi
# içinde belirttiğimizi kullanıyor. Kendi içerisinde 
# NOT! IT'nin raise_percent'ini değiştirmek inherit edildiği class'ınkini değiştirmez.

print(Employee.raise_percent)

# subclass'da yaptığımız değişiklik parent class'ı etkilemez.
# Diyelim ki IT'cilere yeni bir özellik olarak hangi programlama dili bildiklerini de eklemek istiyorum.

class IT(Employee):

    raise_percent = 1.2
    def __init__(self, name, last, age, pay, lang):
       self.name = name
       self.last = last
       self.age = age
       self.pay = pay
       self.lang = lang

it_1 = IT("James", "Hughes", "32", 5000, "python")
print(it_1.lang)

# Yukarıdaki kod yerine aşağıdaki gibi de yapılabilir
class IT(Employee):
    raise_percent = 1.2
    def __init__(self, name, last, age, pay, lang):
        super().__init__(name, last, age, pay)
        self.lang = lang

# Böylece yukarıda aynı kodu tekrar tekrar yazmamış olduk. Zaten superclass'ın init
# methodu yapıyorsa yeniden yazmaya gerek yok.

it_1 = IT("James", "Hughes", "32", 5000, "C++")
print(it_1.lang)
print(it_1.name)

class IK(Employee):
    raise_percent = 1.3
    def __init__(self, name, last, age, pay, experience):
        super().__init__(name, last, age, pay)
        self.experience = experience
    
    def print_exp(self):
        print(f"This employee has {self.experience} years of experience.")

ik_1 = IK("charlie", "brown", "22", 3000, 12)
ik_1.print_exp()

print(isinstance(ik_1, IK))
print(isinstance(ik_1, Employee))
print(issubclass(IK, Employee))
print(issubclass(IT, Employee))
print(issubclass(IT, IK))






