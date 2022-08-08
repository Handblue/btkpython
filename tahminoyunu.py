import random

sayi = random.randint(1,100)

while True:
    tahmin = int(input("Tahmin ediniz: "))
    if tahmin == sayi:
        print("Tebrikler Bildiniz")
        break
    elif tahmin > sayi:
        print("Daha küçük")
    else:
        print("Daha büyük")
print("Oyunu Bitirdiniz.")