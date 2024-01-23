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
def SprawdzCyfry(text):
    for i in text:
        if i!= '1' or i!= '2' or i!= '3' or i!= '4' or i!= '5' or i!= '6' or i!= '7' or i!= '8' or i!= '9' or i!='0':
            return False

def GenPesel():
    plec = int(input("Podaj plec - parzysta=kobieta, nieparzysta=mezczyzna"))
    while plec<0 or plec>100:
            plec = int(input("Podaj plec - parzysta=kobieta, nieparzysta=mezczyzna"))

    rok = int(input("Podaj  rok urodzenia"))
    miesiac = int(input("Podaj miesiac urodzenia"))
    while miesiac<0:
        miesiac = int(input("Podaj miesiac urodzenia"))
    dzien = int(input("Podaj dzien urodzenia"))

    while dzien<0 or dzien>32:
        dzien = int(input("Podaj dzien urodzenia"))
    pesel= ""
    
    if rok>2000:
        miesiac+=int(miesiac) +20
    miesiac = str(miesiac)
    pesel+= rok[2]+rok[3]+miesiac+dzien
    for i in range(0,3):
        x = random.randint(0,9)
        pesel += str(x)
    return pesel

def SprawdzPesel(pesel):
    if len(pesel)!= 11:
        return "ZlyPesel"
    if SprawdzCyfry(pesel)==False:
        return "Zly Pesel"
    rok = pesel[0]+pesel[1]
    miesiac = pesel[2]+pesel[3]
    dzien = pesel[4]+pesel[5]
    plec = pesel[9]
    kontrol = pesel[10]
    text1 = "1379137913" 
    suma =0
    if int(rok)>24 or int(miesiac)<0 or int(miesiac)>32:
        return "zle dane"
    for i in pesel:
        for j in text1:
            suma += i*j
    suma = str(suma)
    if suma[-1]== pesel[-1]:
        return True
    else:
        return False
print(GenPesel())
