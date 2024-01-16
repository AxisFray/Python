import random
class Pracownik:
    def __init__(self,imie,nazwisko,wiek):
        self.imie=imie
        self.nazwisko=nazwisko
        self.wiek=wiek
    def Vis(self):
        print(f"{self.imie} {self.nazwisko} {self.wiek}")
    def Dane(self):
        imie1=input("podaj imie")
        nazwisko1=input("Podaj nazwisko")
        wiek1=input("Podaj wiek")
        self.nazwisko=nazwisko1
        self.imie=imie1
        self.wiek=wiek1


tab = []
class Wojownik:
    def __init__(self,imie):
        self.imie=imie
        self.sila =sila
        self.szybkosc=szybkosc
        self.jedzenie = jedzenie

    szybkosc = random.randint(0,3)
    sila=random.randint(0,3)
    jedzenie= random.randint(0,3)
    def atak(self):
        pass


W1 = Wojownik("Janek")







