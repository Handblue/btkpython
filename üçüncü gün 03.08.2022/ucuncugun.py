
import math
from multiprocessing.sharedctypes import Value
from unittest import result
'''
# sözlük 
sozluk = {
    "beyaz": "white",
    "kırmızı": "red",
    "siyah": "black",
}

print(sozluk["beyaz"])
print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())

for key, value in sozluk.items():
    print(key,value) 

sozluk ["mavi"] = "blue"
print(sozluk)


# set - tuple

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 8, 5, 6,]
print(liste)

yeniliste = set(liste)
print(yeniliste)

a = (1, 2, 1)
print(a)


print(len(["hello"]))
print(len("hello"))

print(len("hello"[0]))
print(len(["hello"][0]))

#fonksiyonlar

def f(x):
    print(2*x)

def g(a):
    print(3*a)

print("hello world")
f(2)
print("hello world")
f(3)
print("hello world")
g(10)


def f(x):
    return 2*x

cevap = f(2)
print(cevap)


def f(x, y):
    result = x + x * y - 1
    return result

print(f(2,3))
print(f(2,10))
print(f(5,10))
'''
'''
# parametre olarak 2 adet int alan, ve küçük olanı return eden, minimum adında fonksiyon yazınız.

def minimum(sayi1, sayi2):
    if sayi1 < sayi2:
        return sayi1
    else:
        return sayi2

# kullanıcıdan 2 adet int alınız. küçük olanı minimum fonksiyonu ile ekrana basınız.
a = int(input("1. sayi: "))
b = int(input("2. sayi"))
print("küçük sayi: ",)
'''


#veri bilimi için notlar
#kaggle (öğrenmek için güzel bir yer) 
#huggingface (kaggleden daha iyi)
#teachable mchine (güzrl yapay zeka)


#gpt-3 
#dall-e

#codeforces
#leetcode (mülakat soruları vs var)

#hackerrank 


# parametre olarak bir sayı alan, ve bu sayının asal olup olmadığını bulan bir fonksiyon yazınız.

# parametre olarak bir sayı alan çift ise true tek ise false dönen bir fonskiyon yazınız.

'''
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def isEven2(number):
    if number % 2 == 0:
        return True
    return False

def isEven3(number):
    return number % 2 == 0
'''
'''
def isPrime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    
    return True


# isPrime metodu kullanarak 900.000 ile 1.000.000 arasındaki asal sayıları bul.
#tüm asal sayıları ekrana basınız.

for i in range(900000, 9100000):
    if isPrime(i):
        print(i)
'''
# parametere olarak bir sayı alan ve bu sayı büyklüğünde yıldız primidi basan fonksiyonu basınız.


def pyramid(n):
    for i in range(n):
        print("* " * (i+1))

pyramid(5)
pyramid(3)
pyramid(10)

# parametre olarak bir sayı alan ve sayının faktoriyelini return eden bir fonksiyon yazınız.

def faktoriyel(sayi):
    cevap = 1
    for i in range(sayi):
        cevap *= (i+1)
    return cevap
print(faktoriyel(5))
print(faktoriyel(4))
print(faktoriyel(15))

math.factorial
