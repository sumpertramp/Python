# Magic Method'ları kullanarak bazı built-in davranışları değiştirebiliriz.
# Magic Methodlar __ ile çevrilidir. Bunlara dunder method da denir.

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

emp_1 = Employee("James", "Hughes", "32", 5000)
emp_2 = Employee("Charlie", "Brown", "22", 3000)

# __init__()
# emp_1 = Employee("James", "Hughes", "32", 5000) gibi class'dan obje oluşturma 
# kısmında çağrılır. Class(.....) formatında input olarak verilenleri arguman
# olarak alır kendine.

# __str__()
# Objenin okunabilir bir tanımını oluşturur.

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
    
    def __str__(self):
        return f"Employee(name={self.name}, last={self.last}, age={self.age}, pay={self.pay} )"

emp_1 = Employee("James", "Hughes", "32", 5000)
emp_2 = Employee("Charlie", "Brown", "22", 3000)

print(emp_1) # Burada okunabilir hale getiren __str__ magic methodu

# __add__()
# Objelerin + operatöründe nasıl davranacağını tanımlamak için add magic methodu kullanılır.

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

    def __add__(self, other):
        return self.pay + other.pay

emp_1 = Employee("James", "Hughes", "32", 5000)
emp_2 = Employee("Charlie", "Brown", "22", 3000)
print(emp_1 + emp_2)

# __len__()
# Classın objesinin boyutunu vermek için kullanılır.

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

    def __len__(self):
        return len(self.name)

emp_1 = Employee("James", "Hughes", "32", 5000)
emp_2 = Employee("Charlie", "Brown", "22", 3000)
print(len(emp_1))
print(len(emp_2))





       
