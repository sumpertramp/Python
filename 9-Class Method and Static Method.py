# @classmethod decorator methodu ilk argüman olarak instance almak yerine class'ı
# alacak şekilde günceller.

class Employee:

    raise_percent = 1.05
    num_emp = 0

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay

        # Burada arttırılır
        Employee.num_emp += 1
    
    def apply_raise(self):
        self.pay = self.pay * Employee.raise_percent

    @classmethod
    def set_raise_percent(self, amount):
        self.raise_percent = amount
    
emp1 = Employee("James", "Hughes", "32", 5000)
emp2 = Employee("Charlie", "Brown", "22", 3000)

Employee.set_raise_percent(1.6)

print(emp1.raise_percent)
print(emp2.raise_percent)
print(Employee.raise_percent)

emp1.set_raise_percent(2.3)

print(emp1.raise_percent)
print(emp2.raise_percent)
print(Employee.raise_percent)

# Alternative Constructor
# Diyelim ki bize class'ı oluştururken input olarak string veriyorlar ve bizim bundan
# name, age gibi bilgileri kendimiz çıkarmamız lazım

emp_1_str = "James-Hughes-32-5000"
emp_2_str = "Charlie-Brown-22-3000"

print(emp_1_str.split("-"))

name, last, age, pay = emp_1_str.split("-")

emp_1 = Employee(name, last, age, pay)

print(emp_1)

# Ama belki her zaman bu şekilde vermeyeceğiz. String olarak input geldiğinde
# objenin bu şekilde oluşması için başka nasıl bir mekanizma kullanabiliriz?
# Her seferinde kendim parse etmek yerine bunu bir method olarak yazabiliriz.

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
    
    @classmethod
    def set_raise(cls, amount):
        cls.raise_percent = amount 
    
    # Yeni çalışan yaratacak ve döndürecek
    @classmethod
    def from_string(cls, emp_str):
        name, last, age, pay = emp_1_str.split("-")
        return cls(name, last, int(age), float(pay))

emp_1_str = "James-Hughes-32-5000"
emp_2_str = "Charlie-Brown-22-3000"
emp_1 = Employee.from_string(emp_1_str)
print(emp_1)
print(emp1.pay)

# Static Method
# Regular Methodlar (ilk gördüğümüz), class instance'ını (oluşturulan objeyi),
# metodlara otomatik olarak argüman olarak veriyordu (self olarak). Class methodları
# class'o otomatik olarak argüman olarak veriyor. Static methodlar otomatik bir 
# şey vermeyeb methodlar olacaktır. 
# İnstance veya class'a methodun ierisinde erişim olmuyorsa static olarak tanımlamak
# daha iyi olabilir.


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
    
    @classmethod
    def set_raise(cls, amount):
        cls.raise_percent = amount 
    
    # Yeni çalışan yaratacak ve döndürecek
    @classmethod
    def from_string(cls, emp_str):
        name, last, age, pay = emp_1_str.split("-")
        return cls(name, last, int(age), float(pay))
    
    @staticmethod
    def holiday_print(day):
        if day == "weekend":
            print("This is an off day.")
        else:
            print("This is not an off day.")

Employee.holiday_print("weekend")
emp_1 = Employee("James", "Hughes", "32", 5000)
print(emp_1.holiday_print("working day"))

