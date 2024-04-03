import random
t = []
for i in range(0,100):
    t.append(random.randint(0,100))
def sortBab():
    print(t)
    for i in range(1,100):
        for j in range(0,100):
            if t[i]>t[j]:
                x = t[i]
                t[i]=t[j]
                t[j] = x
    print(t)
    
def sorWyb():
    print(t)
    for i in range():
        m = i 
        for j in range(i+1, 100): 
            if t[j] < t[m]: 
                m = j 
    print(t)
def sortWst():
    print(t)
    for i in range(1, 100):
        temp = t[i]
        j = i - 1
        # Przesuwanie elementów większych od temp, aby zrobić miejsce dla temp
        while j >= 0 and t[j] > temp:
            t[j + 1] = t[j]
            j -= 1
        # Wstawienie temp na odpowiednie miejsce w posortowanej części listy (tablicy)
        t[j + 1] = temp
        print(t)
def Menu():
    print("1.Sortowanie Babelkowe")
    print("2.Sortowanie przez wybor")
    print("3.Sortowanie przez wstawianie")
    wybor = int(input("Wybierz 1-3"))
    if wybor==1:
        sortBab()
    elif wybor==2:
        sorWyb()
    elif wybor==3:
        sortWst()
    else:
        print("zly wybor")
        Menu()

Menu()