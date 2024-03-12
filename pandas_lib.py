import pandas as pd
import random
lista = []

for _ in range(0,100):
    lista .append(random.randint(0,100))
dane = pd.Series(lista)

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

print(dane.count())
#liczy ile jest kolumn zapelnionych
print(dane[::2][dane>50].count())


