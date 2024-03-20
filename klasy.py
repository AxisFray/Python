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

class figura:
    def __init(self,*boki):
        self.boki = boki
        for el in boki:
            if el<=0:
                print("jeden z bokow jest niewlasciwy")
    




class trojkat(figura):
    def __init(self, a,b,c):
        super().__init(a,b,c)
        if a+b<c:
            if b+c<a:
                if a+c<b:
                    print("Nie da sie utworzyc trojkata")

class czworokat:
    def __init__(self,a=0,b=0,c=0,d=0) -> None:
        self.a =a
        self.b=b
        self.c=c
        self.d=d
    def obwod(self):
        print(f"obwod jest rowny {self.a + self.b +self.c+self.d}")
    
class prostokat(czworokat):
    def __init__(self,a,b):
        super().__init__(self,a,b)
        self.a=a
        self.b=b
    def Pole(self):
        print(f"Pole wynosi {self.a*self.b}")
    def obwod(self):
        print(f"Obwod wynosi {2*(self.a+self.b)}")
        
el1 = prostokat(5,4)
el1.obwod()





