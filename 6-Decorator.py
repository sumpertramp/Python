#Decorators
#Decorator'lar başka fonksiyonları parametre olarak kabul edip yeni br 
#fonksiyonalite ile yeni bir fonksiyon döndüren yapılardır.
#Decorator olarak outher function olarak tanımladığımız şey modifikasyon 
#yapacağımız içeride tanımladığımız aşağıdaki örnekte gösterilen yeni
#fonksiyoneler katacak olan wrapper_func'u outher olarak tanımlanan
#decorator_func obje olarak döndürüyor

def print_func():
    print("Hey!")

def decorator_func(func):
    def wrapper_func():
        return func()
    return wrapper_func #Obje olarak döndürdüğü bura function call () yok

#Bir fonksiyonu input olarak ya da obje olarak döndürebiliriz.               

decorated_print = decorator_func(print_func)
decorated_print()

#Var olan fonksiyona fonksiyonu değiştirmeden yeni bir davranış kazandırma.
def decorator_func(func):
    def wrapper_func():
        print(f"the name of the functions is {func.__name__}")
        return func()
    return wrapper_func

decorated_print = decorator_func(print_func)
decorated_print()

#Yukarıdaki son işlem aşağıdaki ile aynı, başka bir yöntem:
@decorator_func
def print_func():
    print("Hey!")

#Çalışması için çağıralım:
print_func()

def func(name, number):
    print(f"Name:{name}, number:{number}")

func("jack", 102)

#Aşağıda fonksiyona kaç tane argüman vereceğimizi
def decorator_func(func):
    def wrapper_func(*args):
        print(f"the name of the function is {func.__name}")
        return func(*args)
    return wrapper_func

func("Jack", 102) #Burada wrapper_func Jack ve 102 ile çağrılıyor.



