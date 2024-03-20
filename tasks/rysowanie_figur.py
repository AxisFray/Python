x = int(input("Podaj wysokosc prostokata"))
y = int(input("Podaj szerokosc prostokata"))

for i in range(0,x):
    for j in range(0,y):
        if i==0:
            if j==y-1:
                print("*")
            else:
                print("*",end="")
        elif i==x-1:
            print("*",end="")
        elif j==0:
            print("*",end="")
        elif j==y-1:
            print("*")
        else:
            print(" ",end="")
       

h = int(input("Podaj wysokosc"))

p=1
for i in range(0,h):
    for j in range(0,p):
        if j==p-1:
            print("*")
        else:
            print("*",end="")
    p+=1


h=int(input("Podaj wysokosc"))

w = h-1
t=1
for i in range(0,h):
    for j in range(0,w):
        print(" ",end="")
    for k in range(0,t):
        print("*",end="")
    for l in range(0,w):
        if l==w-1:
            print(" ")
        else:
            print(" ",end="")
    t+=2
    w-=1
        
