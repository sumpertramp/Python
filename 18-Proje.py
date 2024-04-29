
# 1 - MERGE SORTED ARRAY (Easy)
# Bu problemde, sıralı iki dizi (nums1 ve nums2) veriliyor ve bu dizileri birleştirerek 
# nums1 içinde sıralı bir şekilde saklamamız isteniyor. nums1 dizisinin ilk m elemanı 
# kullanılarak ve nums2 dizisinin tüm elemanları kullanılarak sonucu bulmamız gerekiyor.
class Solution(object): # ***
    def merge(self, nums1, m, nums2, n):
        # nums1 ve nums2 dizilerinin sonundan başlayarak birleştirme işlemi yapılır
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n-1]
                n -= 1
        # nums2 dizisinde eleman kaldıysa, bunlar nums1'in sonuna eklenir
        while n > 0:
            nums1[n - 1] = nums2[n - 1]
            n -= 1

# 2 - REMOVE ELEMENT (Easy)
# Bu fonksiyo verilen bir nums dizisinden val değerlerini çıkartarak, geri kalan elemanların 
# sayısını ve bu elemanları içeren diziyi döndürür.  
class Solution(object): # **
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    

# 3 - REMOVE DUBLICATES FROM SORTED ARRAY (Easy)
# Bu fonksiyon, verilen nums dizisindeki tekrarlanan elemanları kaldırır ve kalan benzersiz
# dizinin eleman sayısını döndürür.
class Solution(object): # **
    def removeDublicates(self, nums):
        if not nums:
            return 0
        
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k

# 4 - REMOVE DUBLICATES FROM SORTED ARRAY II (Medium)
# Bu fonksiyon, nums dizisinin önceki elemanlarını kullanarak yinelenenlerin sayısını 
# takip eder ve her bir elemanı en fazla iki kez bırakarak nums dizisini günceller. 
# Sonuç olarak, nums dizisindeki ilk k elemanı, yinelenen elemanları en fazla iki kez 
# içerecek şekilde güncellenir.
class Solution(object): # ***
    def removeDublicates2(self, nums):
        if not nums:
            return 0
        k = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[k] = nums[i]
                k += 1
        return k
     
# 5 - MAJORITY ELEMENT (Easy)
# Bu kod, Boyer-Moore Oy Algoritması olarak bilinen bir algoritmayı kullanır. Bu algoritma, 
# çoğunluk elementini lineer zaman karmaşıklığında ve O(1) ekstra alan kullanarak bulmayı 
# sağlar. Algoritma, bir aday element ve bir sayma değişkeni kullanır. Döngü her aday 
# elemente karşı bir sayma yapar ve eğer sayma 0'a düşerse, adayı günceller. Bu şekilde, 
# çoğunluk elementi varsa, son aday çoğunluk elementi olacaktır.
class Solution(object): # ***
    def majorityElement(self, nums):

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate

# 6 - ROTATE ARRAY (Medium)
# Bu fonksiyon, dizi elemanlarının tamamını ters çevirerek dizi içinde dönüşümleri 
# gerçekleştirir. Önce dizinin tamamını ters çevirir, ardından ilk k elemanı ve ardından 
# kalan elemanlar olmak üzere iki ayrı bölümü tekrar ters çevirir. Bu şekilde, diziyi sağa 
# doğru döndürmüş oluruz.

class Solution(object):
    def rotate(nums, k):
        n = len(nums)
        k %= n
    
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

# 7 - BEST TIME TO BUY AND SELL STOCK  (Easy)
# Bu çözümde, listenin ilk fiyatını min_price olarak ayarlıyoruz ve maksimum karı max_profit 
# olarak başlatıyoruz. Daha sonra, listedeki her fiyat için, mevcut fiyatın minimum fiyattan 
# küçük olup olmadığını kontrol ediyoruz. Eğer öyleyse, min_price değerini güncelliyoruz. 
# Aksi takdirde, mevcut fiyatın min_price ile alım yapıldığında elde edilen karı kontrol 
# ediyoruz ve max_profit değerini güncelliyoruz. Sonunda, maksimum karı döndürüyoruz.
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit

# 8 - BEST TIME TO BUY AND SELL STOCK II (Medium)
# Bu çözümde, hisseyi her artan fiyat değişiminde satın alıp satarak karı maksimize etmiş 
# oluruz. Bu şekilde, her artan fiyat değişiminden kar elde ederiz ve toplam karı bulmak 
# için bu karları toplarız. Bu algoritma, her fiyat değişimini tek tek kontrol ettiği için 
# O(n) zaman karmaşıklığına sahiptir, n ise fiyatların sayısını temsil eder.
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
    
# 9 - JUMP GAME (Medium)
# Bu çözüm, bir dizi üzerinde tek seferlik bir döngü ile her adımda ulaşılabilen maksimum 
# indeksi takip eder. Her adımda, mevcut indeks maksimum erişilebilir indeksi geçtiyse 
# (yani oraya ulaşamazsak), False döndürür. Aksi takdirde, maksimum erişilebilir indeksi 
# günceller ve son indekse ulaşılıp ulaşılamayacağını kontrol eder. Bu yaklaşım, her adımda 
# maksimum erişilebilir indeksi güncellediği ve her indeksi en fazla bir kere ziyaret ettiği 
# için O(n) zaman karmaşıklığına sahiptir.
class Solution(object):
    def canJump(self, nums):
        max_reachable = 0
        for i in range(len(nums)):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])
        return True

# 10 - JUMP GAME 2 (Medium)
# Bu kod, her adımda mevcut konumdan en uzak noktaya kadar olan aralıkta mevcut konumunuzu 
# günceller. Bu yaklaşım, her seferinde mevcut adımın sonuna ulaşırken minimum atlama 
# sayısını hesaplar. Bu sayede, dizi boyunca tek bir döngüyle minimum atlama sayısını 
# bulabilirsiniz.
class Solution(object): 
    def canJump(self, nums):
        n = len(nums)
        if n == 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i ==  current_end:
                jumps += 1
                current_end = farthest
        return jumps

# 11 - HINDEX (Medium)
# Bu fonksiyon, her bir alıntı sayısına sahip makale sayısını hesaplayarak ve ardından toplam 
# makale sayısını ve en az h defa alıntılanan makale sayısını karşılaştırarak, araştırmacının 
# h-index'ini O(n) zaman karmaşıklığı ile bulmamızı sağlar.

class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        paper_count = [] * (n + 1)

        for citation in citations:
            paper_count[min(citation, n)] += 1
        
        totol_papers = 0

        for h in range(n, -1, -1):
            total_papers += paper_count[h]
            if total_papers >= h:
                return h
        return 0

# 12 - INSERT DELETE GETRANDOM O(1) (Medium)
# Bu çözümde, val_to_index adında bir sözlük ve values adında bir liste kullanarak her 
# elemanın ekleme ve çıkarma işlemlerini O(1) karmaşıklıkla gerçekleştiriyoruz. getRandom 
# fonksiyonu ise listenin içinden rastgele bir eleman seçiyor.
import random 
class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        index = self.val_to_index[val]
        last_val = self.values[-1]
        self.values[index] = last_val
        self.val_to_index[last_val] = index
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
    
# 13 - PRODUCT OF ARRAY EXCEPT SELF (Medium)
# Bu çözüm, her bir elemanın solundaki ve sağındaki elemanların çarpımını hesaplamak için 
# iki aşamalı bir işlem kullanır. İlk olarak, her elemanın solundaki çarpımı hesaplar ve 
# result dizisine saklar. Ardından, sağ taraftan çarpımları hesaplar ve sonuçları sol 
# taraftaki çarpımlarla birleştirir. Bu şekilde, her bir elemanın solundaki ve sağındaki 
# çarpımları O(n) zaman karmaşıklığında hesaplanır ve ekstra bir dizi kullanılmaz.

class Solution(object):
    def productExceptSelf(nums):
        n = len(nums)
        result = [0] * n
    
        # Sol taraftan çarpımları hesapla
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
    
        # Sağ taraftan çarpımları hesapla ve sonuçları birleştir
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
    
        return result

# 14 - GAS STATION () (Medium)
# Bu çözümde, her bir istasyondan başlayarak döngüyü tamamlayarak dolaşımı sağlayacak bir 
# algoritma kullanabiliriz. Her istasyonu başlangıç noktası olarak düşünüp, o istasyondan 
# döngüyü tamamlamaya çalışabiliriz. Bu şekilde, her istasyonu başlangıç noktası olarak 
# düşündüğümüzde dolaşımın mümkün olup olmadığını kontrol edebiliriz.
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        total_tank, curr_tank = 0, 0
        starting_station = 0

        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                starting_station = i + 1
                curr_tank = 0
        return starting_station if total_tank >= 0 else -1
    
# 15 - 














