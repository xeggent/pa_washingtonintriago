
from HolaMundo import Figura, Triangulo, Cuadrado, Rombo
print("1.- Triangulo")
print("2.- Cuadrado ")
print("3.- Rombo ")
op=int(input("ingrese un numero "))
match op:
    case 1:
        _base=int(input("ingrese un valor para la base: "))
        _altura=int(input("ingrese un valor para la altura: "))
        c=Triangulo(_base,_altura)
        print("el perimetro es ", c.perimetro())
        print("el area es: ", c.area())
        print("La hipotenusa es", c.hipotenusa())
    case 2:
        _base=int(input("ingrese un valor para la base: "))
        _altura=int(input("ingrese un valor para la altura: "))
        r=Cuadrado(_base,_altura)
        print("el perimetro es ", r.perimetro())
        print("el area es: ", r.area())

    case 3:
        diagonal_ma = float(input("Ingresa el valor de la diagonal mayor: "))
        diagonal_me = float(input("Ingresa el valor de la diagonal menor: "))
        rombo = Rombo(diagonal_ma, diagonal_me)
        print("El perimetro es:",rombo.perimetro())
        print("El area es: ",rombo.area())
        print("La suma de mis diagonales es: ",rombo.sumadedmm())
    





