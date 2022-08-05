from itertools import count
import random

sayi = random.randint(1,100)
count = 0
while True:
    count += 1
    tahmin = int(input("Tahmin ediniz: "))
    if tahmin == sayi:
        print("Tebrikler Bildiniz")
        break
    elif tahmin > sayi:
        print("Daha küçük")
    else:
        print("Daha büyük")
print("Oyunu Bitirdiniz. Hamle Sayınız ->", count)
