#Unpacking

l = [1,2,3,4]
print(l)
print(*l)
l1 = [1,2,3,4]
l2 = [20,21]
merged_l = [*l1, *l2]
print(merged_l)

d1 = {"name":"Jake", "number":402}
d2 = {"last_name":"Sky", "grade":74}
#(d1 + d2) <-- Hata!
d_merged = {**d1, **d2}
print(d_merged)

#Key value aynı ise nasıl davrandığına dair örnek:
d3 = {'name':'Jake', 'number': 402}
d4 = {'name':'Sky', 'grade': 74}
d5 = {'name':'B','grade': 45}
#Yukarıdaki örnekte name keyword'u aynı olduğu için merge işlemi yapılırken 
#daha güncel olanı aldı.

d_merged_2 = {**d3, **d4, **d5}
print(d_merged_2)

#Yukarı da görüldüğü gibi en güncel olana göre birleştiriyor.

str_list = [*"Hey! This is a string."]
print(str_list)