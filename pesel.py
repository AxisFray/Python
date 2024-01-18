import random


# przed 200r
#  RR MM DD LLL P K
# L liczba porzadkowa
# P plec parzysta kobieta
# k cyfra kontrolna 1-3-7-9-1-3-7-9-1-3
#po 2000r
# dodac 20 do miesiaca
#
#
#


def GenPesel():
    while plec<0 or plec>100:
        plec = int(input("Podaj plec - parzysta=kobieta, nieparzysta=mezczyzna"))
    rok = int(input("Podaj  rok urodzenia"))
    while miesiac<0:
        miesiac = int(input("Podaj miesiac urodzenia"))
    while dzien<0 or dzien>32:
        dzien = int(input("Podaj dzien urodzenia"))
    pesel= ""
    miesiac = str(miesiac)
    if rok>2000:
        miesiac+=20
    pesel+= rok[2]+rok[3]+miesiac+dzien
    for i in range(0,3):
        x = random.randint(0,9)
        pesel += str(x)
    return pesel

def SprawdzPesel(pesel):
    if len(pesel)!= 11:
        return "ZlyPesel"
    rok = pesel[0]+pesel[1]
    miesiac = pesel[2]+pesel[3]
    dzien = pesel[4]+pesel[5]
    plec = pesel[9]
    kontrol = pesel[10]
    
    if int(rok)>24 or int(miesiac)<0 or int(miesiac)>32:
        return "zle dane"

