
A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7
H = 8
I = 9
def Change(num):
    num = "X"
def SetPos():
    global arg,A,B,C,D,E,F,G,H,I,num
    costam = input("gdzie ruszasz?")
    if costam == 1:
        Change(A)
    elif costam == 2:
        Change(B)
    elif costam == 3:
        Change(C)
    elif costam == 4:
        Change(D)
    elif costam == 5:
        Change(E)
    elif costam == 6:
        Change(F)
    elif costam == 7:
        Change(G)
    elif costam == 8:
        Change(H)
    elif costam == 9:
        Change(I)
def Board():
    print(A ," | ", B , " | " , C)
    print(D ," | ", E , " | " , F)
    print(G ," | ", H , " | " , I)
    

Board()

