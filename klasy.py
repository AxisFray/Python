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
        self.sila = random.randint(0,3)
        self.szybkosc=random.randint(0,3)
        self.jedzenie = random.randint(0,3)

    def atak(self):
        if tab[0] ==self.imie:
            suma=0
            suma = tab[1].sila + tab[1].szybkosc + tab[1].jedzenie
            suma1 = self.sila+self.szybkosc + self.jedzenie
            if suma>suma1:
                self.smierc()
            else : self.zwyciestwo()
    
    def smierc(self):
        print(f"Umarles {self.imie}")
    def zwyciestwo(self):
        print(f"Zwyciezasz!  {self.imie}")


tab.append(Wojownik("Franek"))
tab.append(Wojownik("Janek"))


tab[0].atak()






