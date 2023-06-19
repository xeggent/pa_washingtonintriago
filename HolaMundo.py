import math
class Figura:
    def __init__(self, base, altura):
        self.__base=base
        self.__altura=altura
    def setbase(self,base):
        self.__base=base
    def getbase(self):
        return self.__base
    def setaltura(self,altura):
        self.__altura=altura
    def getaltura(self):
        return self.__altura
    def hipotenusa(self):
        return math.sqrt((self.getbase()**2)+(self.getaltura()**2))
    def area(self):
        return 0;
    def perimetro(self):
        return 0;
class Triangulo(Figura):
    def __init__(self, base, altura):
        super().__init__(base,altura)
    def perimetro(self):
        return self.getbase()+self.getaltura()+self.hipotenusa()    
    def area(self):
        return self.getbase()*self.getaltura()/2

    

class Cuadrado(Figura):
    def __init__(self, base, altura):
        super().__init__(base,altura)
    def perimetro(self):
        return 2*self.getbase()+2*self.getaltura()   
    def area(self):
        return self.getbase()*self.getaltura()
class Rombo(Figura):
    def __init__(self, diagonal_ma, diagonal_me):
        self.__diagonal_ma = diagonal_ma
        self.__diagonal_me = diagonal_me

    def set_diagonal_ma(self, diagonal_ma):
        self.__diagonal_ma = diagonal_ma

    def get_diagonal_ma(self):
        return self.__diagonal_ma
    

    def set_diagonal_me(self, diagonal_me):
        self.__diagonal_me = diagonal_me
    
    def get_diagonal_me(self):

        return self.__diagonal_me
    
    def perimetro(self):
        return 4 * self.get_diagonal_me()
    
    def area(self):
        return (self.get_diagonal_ma()*self.get_diagonal_me())/2
    
    def sumadedmm(self):
        return (self.get_diagonal_ma()+self.get_diagonal_me())
    
