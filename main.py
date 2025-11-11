#1-misol
lugat1 = eval(input("1-lug‘atni kiriting: "))
lugat2 = eval(input("2-lug‘atni kiriting: "))
birlashtirilgan = {**lugat1, **lugat2}
print("Birlashtirilgan lug‘at:", birlashtirilgan)

#2-misol
lugat = eval(input("Lug‘at kiriting: "))
kalit = max(lugat, key=lugat.get)
print("Eng katta qiymatga ega kalit:", kalit)

#3-misol
lugat = eval(input("Lug‘at kiriting: "))
almashtirilgan = {v: k for k, v in lugat.items()}
print("Almashtirilgan lug‘at:", almashtirilgan)

#4-misol
lugat = eval(input("Lug‘at kiriting: "))
juftlar = {k: v for k, v in lugat.items() if v % 2 == 0}
print("Juft qiymatlarga ega lug‘at:", juftlar)

#5-misol
lugat = eval(input("Lug‘at kiriting: "))
kalit = max(lugat, key=len)
print("Eng uzun kalit:", kalit)
