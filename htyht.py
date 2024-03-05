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
