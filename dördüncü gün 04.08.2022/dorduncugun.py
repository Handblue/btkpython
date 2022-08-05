## ASCII kodları
print(ord('a')) 
print(ord('b'))
print(ord('c'))
print(ord('d'))

print(chr(97))

text = "hello world"

for i in text:
    print(chr(ord(i)+3))

# parametre olarak bir text ve sayı alan, metni sayı kadar sağa kaydıran ve return eden bir sezar şifreleme fonksiyonu yazınız.

def sezarsifreleme(text, number):
    newtext = ""
    for i in text:
        newtext += (chr(ord(i) + number))
    return newtext
print(sezarsifreleme("merhaba",3)) # şifreleme  # şifrelenmiş şifreyi alıp at satırda olan tırnak içine yapıştırdım ve çözdü.
print(sezarsifreleme("phukded",-3)) # çözme

#istenilen sayıyı bul ve kaç kere geçtiğini yaz.

liste = [45,75,65,85,15,25,66,3,2,8,6,15]
arananSayi = 15
bulduMu = False
count = 0

for i in liste:
    if i == arananSayi:
        count += 1
        print("Sayı Bulundu!")
        bulduMu = True
        

if not bulduMu:
    print("Sayı bulunmadı: ")
print("Hamle Sayınız ->", count)

#parametre olarak, bir liste ve bir sayı alan bir fonksiyon yazınız.
#bu fonsksiyon liste içerisinde sayıların kaç kere geçtiğini bulup return etsin.

def search(liste, sayi):
    count = 0

    for i in liste:
        if i == sayi:
            count += 1
    return count

liste = [45,75,65,85,15,25,66,3,2,8,6,15]
print(search(liste, 15))         
print(search(liste, 5))   

# parametre olarak bir liste alan ve bu listeyi sıralayıp return eden bir fonskiyon yazınız.

def sort(liste):
    yeniListe = []
    while len(liste) > 0:
        enbuyuk = max(liste)
        yeniListe.append(enbuyuk)
        liste.remove(enbuyuk)
        print(yeniListe)
    return yeniListe
liste = [45,75,65,85,15,25,66,3,2,8,6,15]
print(sort(liste))

# try except     #hata

try:
    print(1 + "1")
except:
    print("hata")
print("*******")

# özyinelemeli fonksiyolar

def exampleRecursion(n):
    if n == 0:
        return
    print(n)
    exampleRecursion(n-1)  # nerede işimize yarar? bir problemi alt probleme bölmek için kullanılıyor. 
    print(n)
exampleRecursion(5)

#

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))

#class

class Personel():
    def __init__(self) -> None:
        pass