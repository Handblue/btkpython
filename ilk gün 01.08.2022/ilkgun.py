from cgitb import text
from operator import truediv


number = 6

print(number)
print(type(number))   # diğer türlü yazılım şekli: print(number, type(number))  bu şekilde yan yana da yazılabilir.

ornek_bool = True
print(ornek_bool)

metin = "merhaba dünya"
print(metin, type(metin))

a = 3.5
print(3.5,type(3.5))

print(5 / 2)
print(5 // 2)
print(3 + 5)
print(3 - 5)

print(2 ** 3)
print(100 ** 0.5)

print(5 + 2 / 4)
print((5+2) / 4)

print(5 == 5)
print(5 != 5)
print(5 > 4)
print(5 < 4)

sayi = 5
sayi = sayi + 1
print(sayi)

sayi +=1
print(sayi)

sayi *=1
print(sayi)

print(True and False)
print(True or False or False)  # True False yerine sıfır ve bir yazılabilir
print(not True)

# gelir = input("Gelirinizi giriniz: ")
# gelir = int(gelir)
# vergi_yuzdesi = 0.18
# vergi = gelir * vergi_yuzdesi

# print("gelir verginiz: ", vergi)

print('merhaba"dünya"')

# ' I'm using single quotes, but this will create an error' # burada bir sorun var sorunun çözümü \ koymak 
' I\'m using single quotes, but this will create an error' # sorun çözüldü

metin = "merhaba dünya"
print(metin)
print(len(metin))
print(type(metin))
print(metin.upper())


metin = "merhaba dünya"
print(metin[0])
print(metin[1])
print(metin[12])
# print(metin[13])  # hata verdi çünkü o  aralıkta değil 12 ye kadar. Sıfıradan başladığı için
print(metin[-1]) # eksi dediğimiz için sondan başladı saymaya.
print(metin[-2])

print(metin[0:3]) # sadece mer bastırdı.
print(metin[8:len(metin)]) # 8 ve 12 arasını bastırdı. çıktısı dünya.

print(metin[8:13:2]) # dna yazdırdı.


#kullanıcıdan input olarak bir metin alın.
#metin çift indexleri bassın.

# abcdee = input("metin giriniz: ")
# print(abcdee[0:len(metin):2]) 
# print(abcdee[::2])
# print(abcdee[1::2]) # tek sayıları bastırma.

text1 = "hello"
text2 = "word"
text3 = text1 + " " + text2
print(text3)


a = 5
if a < 3:
    print("a 3 den büyük")
elif a==3:
    print("a 3e eşit")
else:
    print("a 3 den büyük")

# a = int(input("sayı giriniz: "))
# if a < 3:
#     print("a 3 den büyük")
# elif a==3:
#     print("a 3e eşit")
# else:
#     print("a 3 den büyük")


for i in range(100):
    print(i)   # sıfırıdan 99 a kadar sayıları ekrana yazdırdı.


# yaslar_toplami = 0
# for i in range(3):
#     dogum_tarihi = input("dogum tarihi: ")
#     yaslar_toplami += 2022 - int(dogum_tarihi)

# print(yaslar_toplami / 3)

metin = "merhaba dünya"
print(metin[5:])
print(metin[0:5])
print(metin[::2])
print(metin[::3])
print(metin[::-1])

metin = "merhaba dünya"
print(metin.upper())
print(metin.lower())
print(metin.capitalize())
print(metin.title())
print(metin.swapcase())
print(metin.count("a"))
print(metin.find("a"))

for i in range(5):
    print(i, metin[i])

'''
ödev 
1- bir metindeki "a" karakter sayısını for loop ile bulunuz.
2- kullanıcıdan 5 adet sayı alınız ve ortalamsını ekrana basınız.
3- input olarak bir metin alan, ve ilk harfini büyük, kalanları küçük yazdıran kodu yazınız.
'''
