'''
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(liste[4]) #4. indexi gösteriyor.
print(liste[1::2]) # çift sayıları listeleriyor.
print(liste[::2]) # tek sayıları listeliyor.

print(len(liste)) 
print(sum(liste))
print(max(liste)) # max değer
print(min(liste)) # min değer

#yukarıdaki listenin ortlamasını prinit ile bulunuz
#yukarıdaki listenin  ilk yarısını toplayınız son yarısının toplamının farkını prnt ediiz
#yukarıdaki listenin en büyük ve en küçük sayısının farkını print ediniz.

print(sum(liste) / len(liste))

print(max(liste) - min(liste))

ilkyarisi = liste[:len(liste) // 2]
sonyarisi = liste[len(liste) // 2:]
print(sum(ilkyarisi) -sum(sonyarisi))



liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste2 = [20,30,40]

yeniliste = liste + liste2 
print(yeniliste)


print(list(range(20))) #range aralık demek   ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
print(list(range(10, 20))) #                 ([10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
print(list(range(10, 20, 2))) #              ([10, 12, 14, 16, 18])


#range metodu ile 0,100 arasındaki tüm çift sayıları ekrana bastırınız.
#range metodu ile 100,200 arasındaki tüm tek sayıları ekrana bastırınız.
#1000 den 0 a kadar 100ün katlarını tersten ekrana bastırınız. 

print(list(range(0,100,2)))
print(list(range(101,200,2)))
print(list(range(1000,-1,-100)))


for i in range(100):   # i yerine her şey yazılabilir 
    print(i)


#sıfırdan 50 ye kadar tüm çift sayıların karesini ekrana basınız.

for sayi in range(0,50,2):
    print(sayi**2)    # ek çözüm print (sayi * sayi)


liste = [1, 2, 3, 4, 5]
print(liste)

liste.append(10) # listemize 10 ekledik
print(liste)

liste.insert(0, 20) # 0. indexten sonra 20i ekle dedik
print(liste)

liste.sort() # sayısal büyüklük olarak sıralanır.
print(liste)

liste.sort(reverse=True)
print(liste)

print(liste.pop()) # eleman silme
print(liste)

print(liste.pop(0)) # sıfırıncı indexteki eleman silinir.
print(liste)


#insert kullanarak, append(99) yapınız.

print(liste)
liste.insert(len(liste), 99)
print(liste)


liste.reverse()
print(liste)

#  https://www.w3schools.com/python/python_ref_list.asp
#  https://docs.python.org/3/tutorial/datastructures.html

liste = [1, 2, 3, 4, 5]

yeniliste = []
for i in range(len(liste)):
    yeniliste.append(liste[i] ** 2)
print(yeniliste)
                     # 2 farklı yapım yolu
yeniliste = []
for i in liste:
    yeniliste.append(i ** 2)
print(yeniliste)

# list comprehension ile yenilistenin tüm elemanlarını 1 arttırın.

yeniliste2 = [i + 1 for i in yeniliste]
print(yeniliste2)

yeniliste3 = [i / 2  for i in yeniliste]
print(yeniliste3)

'''

##########################################
'''
yas = int(input("yaşınızı giriniz: "))

if yas < 0 or yas > 120:
    print("yaşınız geçersiz")
elif yas >=0 and yas <= 7:
    print("okula gitmiyorsun")
elif yas >=8 and yas <= 13:
    print("ilkokula gidiyorsun")
elif yas >=14 and yas <= 18:
    print("liseye gidiyorsun")
elif yas >=19 and yas <= 25:
    print("üniversiteye gidiyorsun")
else:
    print("işe gidiyorsun")
'''
'''
sayi = 0
while sayi < 100:
    print(sayi)
    sayi += 2
    if sayi > 50:
        break

number = 0 
while number != -1:
    number = int(input("bir sayi gir: "))
    print(number)
'''
'''
#-1 de çık daha önce girilen sayıları ekrana bas ve ortalamarını bul.

number = 0
liste = [] 
while number != -1:
    number = int(input("bir sayi gir: "))
    print(number)

    if number != -1:
        liste.append(number)
print(liste)

print(max(liste))
print(min(liste))
print(sum(liste))
print(len(liste))
'''
##########################################

import random

print(random.randrange(1,10))
print(random.randrange(1,10))
print(random.randrange(1,10))

liste = [x for x in "abdsdfşigkdlfshklkalaf"]
print(random.choice(liste))

#kullanıcıdan input alarak bir isim alın. bu ismin hafleri ile ve rakamlar ile random bir parola oluşturun. 
#parola 10 haneli olsun büyük harfler olabilir.

isim = input("isminizi girin: ")
isim = isim.lower() + isim.upper() + "0123456789"
password = ""
for i in range(10):
    password += random.choice(isim)
print(password)

#ödevvv 
# 1- kullanıcıdan 2 adet input alınız. bu iki  sayıyı karşılaştırıp ekrana "küçük sayı x büyük sayı y" şeklinde yazdırınız.
# 2- hileli bir zar yapınız. Bu zar %50 ihtimalle 6 gelsin.
# 3- 0 dan 100e kadar 7 nin kartlarını range ile yazınız
# 4- 0 dan 100e kadar 7 nin katlarını for ile yazınız  
# 5- 0 dan 100e kadar 7 nin katlarını while loop ile yazınız
# 6- 0 dan 100e kadar 7 nin katlarını bir listeye alınız. Bu listedeki tüm elemanların karesini ekrana yazınız.
# 
# yarın
# functions
# dict
# set, tuple  




