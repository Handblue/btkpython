from convert import convertWeekDays

#class

class Personel():
    def __init__(self, isim, soyisim):
        self.isim = isim
        self.soyisim = soyisim

    def Selamla(self):
        print("merhaba", self.isim, self.soyisim)

per1 = Personel("ahmet", "yıldız")
per1.Selamla()

# isim soyisim, yas, cinsiyet, maas, tckimlik, özelliklerini ekle
#ardından 3 tane personel nesnesi tanımlayınız.

class Personel():
    def __init__(self, isim, soyisim, yas, cinsiyet, maas, kimlik, calisma_gunleri):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.cinsiyet = cinsiyet
        self.maas = maas 
        self.kimlik = kimlik
        self.calisma_gunleri = calisma_gunleri

    def printInfo(self):

        print(self.isim, self.soyisim, self.yas, "yaşındadır.")
        print(self.cinsiyet,"cinsiyetindedir.")
        print("maası", self.maas, "TL'dir.")
        print("kimlik numarası", self.kimlik)
        gunler = [convertWeekDays[i] for i in self.calisma_gunleri]
        print("calısma günleri:", ' / '.join(gunler))

    def maas_guncelleme(self, yeni_maas):
        self.maas = yeni_maas

    def calisma_gunu_ekle(self, gun):
        self.calisma_gunleri.append(gun)     

per1 = Personel("ahmet", "yıldız", 32 , "M", 200, "10002546302",[1,2])
per2 = Personel("ayse", "fatma", 52 , "F", 2000, "10002546305",[3,4])
per1.printInfo()
per1.maas_guncelleme(5000)
per1.calisma_gunu_ekle(6)
per2.printInfo()
