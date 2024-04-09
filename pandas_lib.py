import pandas as pd
import random
lista = []

for _ in range(0,100):
    lista .append(random.randint(0,100))
dane = pd.Series(lista)

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





