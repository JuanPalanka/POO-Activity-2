import math


class Circulo:
    def __init__(self, radio: int):
        self.radio = radio

    def calcular_area(self) -> float:
        return math.pi * (self.radio**2)

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return (2 * self.base) + (2 * self.altura)

class Cuadrado:
    def __init__(self, lado: int):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado * self.lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return self.base * self.altura // 2

    def calcular_hipotenusa(self) -> float:
        return math.pow(self.base * self.base + self.altura * self.altura, 0.5)

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self) -> None:
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura and self.base == hipotenusa and self.altura == hipotenusa:
            print("Es un triángulo equilátero")
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")

class Rombo:
    def __init__(self, diagonal_mayor: int, diagonal_menor: int, lado: int):
            self.diagonal_mayor = diagonal_mayor
            self.diagonal_menor = diagonal_menor
            self.lado = lado

    def calcular_area(self) -> float:
            return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self) -> float:
            return 4 * self.lado


class Trapecio:
    def __init__(self, base_mayor: int, base_menor: int, altura: int, lado1: int, lado2: int):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self) -> float:
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def calcular_perimetro(self) -> float:
        return self.base_mayor + self.base_menor + self.lado1 + self.lado2

figura1 = Circulo(2)
figura2 = Rectangulo(1, 2)
figura3 = Cuadrado(3)
figura4 = TrianguloRectangulo(3, 5)
figura5 = Rombo(8, 6, 5)
figura6 = Trapecio(10, 6, 4, 5, 5)

print(f"El área del círculo es = {figura1.calcular_area()}")
print(f"El perímetro del círculo es = {figura1.calcular_perimetro()}")
print()
print(f"El área del rectángulo es = {figura2.calcular_area()}")
print(f"El perímetro del rectángulo es = {figura2.calcular_perimetro()}")
print()
print(f"El área del cuadrado es = {figura3.calcular_area()}")
print(f"El perímetro del cuadrado es = {figura3.calcular_perimetro()}")
print()
print(f"El área del triángulo es = {figura4.calcular_area()}")
print(f"El perímetro del triángulo es = {figura4.calcular_perimetro()}")
figura4.determinar_tipo_triangulo()
print()
print(f"El área del rombo es = {figura5.calcular_area()}")
print(f"El perímetro del rombo es = {figura5.calcular_perimetro()}")
print()
print(f"El área del trapecio es = {figura6.calcular_area()}")
print(f"El perímetro del trapecio es = {figura6.calcular_perimetro()}")