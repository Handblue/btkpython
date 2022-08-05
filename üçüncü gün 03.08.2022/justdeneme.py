def listeortalama(liste):
    return sum(liste) / len(liste)
print(listeortalama([1,2,3,4,5]))
print(listeortalama([1,2,3,4,5,6,7,8,9]))


def yontem1():
    #kullanıcaıdan input olarak liste alma yöntem 1
    liste = []
    while True:
        sayi = input("sayi giriniz: ")
        if sayi == "":
            break
        liste.append(int(sayi))
    print(liste)

def yontem2():
    # kullanıcıdan input olarak liste alma yöntem 2
    liste = []
    uzunluk = int(input("liste uzunluğu: "))
    for i in range(uzunluk):
        sayi = int(input("sayi giriniz: "))
        liste.append(sayi)
    print(liste)

def yontem3():
    # kullanıcıdan input olarak liste alma yöntem 3
    str_list = input("liste giriniz: ")
    liste = str_list.split(" ")
    liste = [int(i) for i in liste]
    print(liste)