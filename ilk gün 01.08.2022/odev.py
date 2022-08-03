'''
ödev 
1- bir metindeki "a" karakter sayısını for loop ile bulunuz.
2- kullanıcıdan 5 adet sayı alınız ve ortalamsını ekrana basınız.
3- input olarak bir metin alan, ve ilk harfini büyük, kalanları küçük yazdıran kodu yazınız.
'''

#soru1
metin = "merhaba dünya"
counter = 0
for i in range(len(metin)):
    if metin[i] == 'a':
        counter += 1
print(counter)


#soru 2
sayi1 = int(input("1. sayı: "))
sayi2 = int(input("2. sayı: "))
sayi3 = int(input("3. sayı: "))
sayi4 = int(input("4. sayı: "))
sayi5 = int(input("5. sayı: "))

toplam = sayi1 + sayi2 + sayi3 + sayi4 + sayi5
ortalama = toplam / 5 
print(ortalama)

#soru3
metin = input("metin gir: ")
metin = metin[0].upper() + metin[1:].lower()
print(metin)

