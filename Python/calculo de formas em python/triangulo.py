class Triangulo:
    def __init__(self,l1,l2,l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

        self.semiperimetro = 0

    def set_lado(self,l1,l2,l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def semip(self):
        self.semiperimetro = (self.l1+self.l2+self.l3)/2
    

    def calcular_area(self):
        self.semip()

        area =  (self.semiperimetro*(self.semiperimetro-self.l1)*(self.semiperimetro-self.l2)*(self.semiperimetro-self.l3))

        area = area**0.5
        return area

