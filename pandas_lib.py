import pandas as pd
import random
lista = []

for _ in range(0,100):
    lista .append(random.randint(0,100))
dane = pd.Series(lista)

a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
#argumenty to kolumny, indeksy

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
#tutaj indeksami będą przypisane wartosci w słowniku

mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000}]
df = pd.DataFrame(mydict)
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000

print(dane.to_string())
#wyswietlanie wszystkich danych

print(dane.loc[:100])
#wyswietla 100 rekordow

print(dane.head(10))
#print pierwsze 10 elementow

print(dane.tail(10))
#print 10 ostatnich elmentow

print(dane.min())
# wartosc minimalna

print(dane.max())
#wartosc maksymalna

print(dane.mean())
#srednia

print(dane.median())
#wartosc srodkowa

print(dane.info())
#wyswietla informacje o danych

print(dane[1:50:3])
#print elementy od 1 do 50 co 3
print(dane[::2])
#print dane co 2
print(dane[3:])
#wypisz dane od 3
print(dane[:2])
#wypisz dane bez ostatnich 2

print(dane.count())
#liczy ile jest kolumn zapelnionych
print(dane[::2][dane>50].count())

dane.rename(columns={"kol1":"kol2"},inplace=True)
#zmiana nazwy kolumny

dane["imie"] = dane["imie"].map(funkcja)
#map przechodzi przez wszystkie rekordy i wykonuje na nich funkcję

print("---------------------------")
l1 =[]
for _ in range(0,100):
    l1 .append(random.randint(0,100))
dane1 =pd.Series(l1)
print(f"srednia  to { dane1.mean()}")

slownik = {"apples":32,"bananas":534,"grapes":344}
dane2 = pd.Series(slownik)

miesiace= {
    "polish": ["styczen","luty","marzec","kwiecien","maj","czerwiec",
                "lipiec","sierpien","wrzesien","pazdziernik","listopad","grudzien"],
    "days" :  [31,28,31,30,31,30,31,31,30,31,30,31]
}
dane3 = pd.Series(miesiace)

#wczytywanie plikow csv jako listy
csv = pd.read_csv("Pracownicy 2.csv",sep=",")
print(csv)

json = pd.read_json("Pracownicy 2.json",sep=',')
print(json)





