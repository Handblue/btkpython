#ödevvv 
# 1- kullanıcıdan 2 adet input alınız. bu iki  sayıyı karşılaştırıp ekrana "küçük sayı x büyük sayı y" şeklinde yazdırınız.
# 2- hileli bir zar yapınız. Bu zar %50 ihtimalle 6 gelsin.
# 3- 0 dan 100e kadar 7 nin kartlarını range ile yazınız
# 4- 0 dan 100e kadar 7 nin katlarını for ile yazınız  
# 5- 0 dan 100e kadar 7 nin katlarını while loop ile yazınız
# 6- 0 dan 100e kadar 7 nin katlarını bir listeye alınız. Bu listedeki tüm elemanların karesini ekrana yazınız.

'''
#soru 1
sayi1 = int(input("1. sayi:"))
sayi2 = int(input("2. sayi:"))

if sayi1 > sayi2:
    print("küçük sayi", sayi2,"ve büyük sayı", sayi1)
    print("küçük sayi " + str(sayi2) + " ve büyük sayi " + str(sayi2))
    print("küçük sayı {} ve büyük sayı {}".format(sayi1,sayi2))
else:
    print("küçük sayi", sayi1,"ve büyük sayı", sayi2)
    print("küçük sayi " + str(sayi2) + " ve büyük sayi " + str(sayi2))
    print("küçük sayı {} ve büyük sayı {}".format(sayi1,sayi2))                   # else kısımı düzenlenecek
'''


'''
#soru 2
import random            # çözüm 1 
liste = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6]
print(random.choice(liste))                   
'''

'''
import random              # çözüm 2

liste = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6]
deneysayisi = 100
deneysonuclari = []
for i in range(deneysayisi):
    deney = random.choice(liste)
    deneysonuclari.append(deney)

print(deneysonuclari.count(1) / deneysayisi)
print(deneysonuclari.count(2) / deneysayisi)
print(deneysonuclari.count(3) / deneysayisi)
print(deneysonuclari.count(4) / deneysayisi)
print(deneysonuclari.count(5) / deneysayisi)
print(deneysonuclari.count(6) / deneysayisi)
'''
'''
import random    # çözüm 3 
sayi = random.randint(1, 2)
if sayi == 1:
    print(6)
else:
    print(random.randint)
'''
'''
print(list(range(0,100,7)))  # soru 4
'''
'''
for i in range(0,100,7): # soru 5
    print(i)
'''
'''
i = 0        # soru 5 yavaş çözüm
while i < 100:
    if i % 7 == 0:
        print(i)
    i += 1
'''
'''
import datetime  # soru 5 hızlı 

start_time = datetime.datetime.now()
i = 0
while i < 1000000:
    print(i)
    i += 7

end_time = datetime.datetime.now()
'''
'''
liste = list(range(0 , 100, 7))  # soru 6 çözüm
 for i in liste:
    print( i * i)

print([i*i for i in liste])

'''