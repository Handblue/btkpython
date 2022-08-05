# def listeortalama(liste):
#     return sum(liste) / len(liste)

def question3():
    for i in range(2,100):
        liste = list(range(1, i+1))
        print(liste)

# def factorial(n):
#     cevap *=i


############################
# for i in range(1,20):
#     factorial(i)

###########################
def maximum1(liste):
    return max(liste)

def maximum2(liste):
    enbuyuk = liste[0]
    for i in liste:
        if i > enbuyuk:
            enbuyuk = i
    return enbuyuk

print(maximum1([31, 22, 13, 84, 75, 6, 47, 8, 19, 10]))
print(maximum2([1, 20, 3, 24, 54, 6, 57, 8, 99, 10]))


def minimum1(liste):
    return min(liste)

def minimum2(liste):
    enkucuk = liste[0]
    for i in liste:
        if i < enkucuk:
            enkucuk = i
    return enkucuk

print(minimum1([31, 22, 13, 84, 75, 6, 47, 8, 19, 10]))
print(minimum2([1, 20, 3, 24, 54, 6, 57, 8, 99, 10]))