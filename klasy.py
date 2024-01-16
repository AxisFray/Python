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

p1 = Pracownik
p1.Dane(p1)
p1.Vis(p1)