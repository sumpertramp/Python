#Closure
#Varsayalım ki bir fonksiyonumuz var ve bu fonksiyonun içerisinde başka bir fonksiyon
#tanımladık, yani bir dış fonksiyonumuz bir de iç fonksiyonumuz var.
#Outer(dış) fonksiyonu çağırdıktan sonra bile inner(iç) fonksiyonun dış
#fonksiyonun scobuna erişebilmesine Closure denir.

def outer():
    msg = "Hey"
    def inner():
        print(msg)
    return inner()

outer()
#Yukarıdaki örnek daha önce yaptıklarımızdan farklı değil. Burada inner 
#fonksiyon enclosing scope a erişip msg değişkenini bastırabildi.

def outer():
    msg = "Hey"

    def inner():
        print(msg)
    return inner

#Yukarıdaki örnekte inner fuction'u obje olarak döndürmemize rağmen msg heyi çağırdı.

