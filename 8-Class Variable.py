# İnstance Variable: Class'tan yaratılan objelerin kendilerine özgü değişkenlerine denir.
# Class Variable: Class'tan yaratılan ve tüm objelerle paylaşılan değişkenlere denir.
# İnstance variable her obje için farklı olabilir, ama class variable hepsi için aynı olmalıdır.
# Tüm çalışanlar arasında hangi verinin paylaşılmasını isteyebilirim? Mesela
# şirket herkese aynı yüzdelik zam uyguluyorsa unun yüzdesini class variable 
# olarak tutabiliriz.

class Employee:

    raise_percent = 1.05

    def __init__(self, name, last, age, pay):
        self.name = name
        self.last = last
        self.age = age
        self.pay = pay
    
    def apply_raise(self):
        self.pay = self.pay * Employee.raise_percent
    
emp_1 = Employee("James", "Hughes", "32", 5000)
emp_2 = Employee("Charlie", "Brown", "22", 3000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
print(emp_2.pay)

# Objenin attribute'larını döndürmek iiçin:
print(emp_1.__dict__)

# Yeni attribute sonradan ekleme, burada sadece emp_1'i günceller.
emp_1.experience = 10
print(emp_1.__dict__)

# Hepsinin raice_percent aynı mı?
print(emp_1.raise_percent)
print(emp_2.raise_percent)
print(Employee.raise_percent)

# Class variable'ı Class üzerinde güncellemek hepsinde günceller.
Employee.raise_percent = 1.06

# Güncelledi mi?
print(emp_1.raise_percent)
print(emp_2.raise_percent)
print(Employee.raise_percent)

# Kaç tane çalışan olduğunu class variable oalrak tutmak
# Her yeni çalışan eklendiğinde toplam çalışanı 1 artırmak istiyoruz.

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

print(Employee.num_emp)
emp_1 = Employee("James", "Hughes", "32", 5000)
print(Employee.num_emp)
emp_2 = Employee("Charlie", "Brown", "22", 3000)
print(Employee.num_emp)






