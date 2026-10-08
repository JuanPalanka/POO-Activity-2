from enum import Enum

class TipoA(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"

class TipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"

class TipoCom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"


class Automovil:
    def __init__(self, marca: str, modelo: int, motor: int,
                 tipo_combustible: TipoCom, tipo_automovil: TipoA,
                 numero_puertas: int, cantidad_asientos: int,
                 velocidad_maxima: int, color: TipoColor, Es_Automatico: bool, valor_multas: int,
                 total_multas: int):

        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible.name
        self.tipo_automovil = tipo_automovil.name
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color.name
        self.velocidad_actual = 0
        self.Es_Automatico= Es_Automatico
        self.valor_multas= valor_multas
        self.total_multas= total_multas
        

    def acelerar(self, incremento_velocidad: int):
        if self.velocidad_actual + incremento_velocidad <= self.velocidad_maxima:
            self.velocidad_actual += incremento_velocidad
        else:
            self.velocidad_actual += incremento_velocidad
            print("El vehiculo ha sido multado por superar el limite de velocidad")
            self.total_multas+=1

    def Multas(self):
        pagar= self.total_multas*self.valor_multas
        print(f"Debes pagar: ${pagar} por {self.total_multas} multa/s por exceso de velocidad")


    def desacelerar(self, decremento_velocidad: int):
        if (self.velocidad_actual - decremento_velocidad) >= 0:
            self.velocidad_actual -= decremento_velocidad
        else:
            print("No se puede decrementar a una velocidad negativa")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia: int) -> float:
        if self.velocidad_actual == 0:
            return float('inf') 
        return distancia / self.velocidad_actual

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipo_combustible}")
        print(f"Tipo de automóvil = {self.tipo_automovil}")
        print(f"Número de puertas = {self.numero_puertas}")
        print(f"Cantidad de asientos = {self.cantidad_asientos}")
        print(f"Velocidad máxima = {self.velocidad_maxima}")
        print(f"Color = {self.color}")
        print(f"Es automatico = {self.Es_Automatico}")

auto1 = Automovil("Ford", 2018, 3, TipoCom.DIESEL, TipoA.EJECUTIVO, 5, 6, 250, TipoColor.NEGRO, True, 180000, 0)

auto1.imprimir()
auto1.velocidad_actual = 100
print(f"Velocidad actual = {auto1.velocidad_actual}")

auto1.acelerar(200)
print(f"Velocidad actual = {auto1.velocidad_actual}")

auto1.Multas()

auto1.desacelerar(50)
print(f"Velocidad actual = {auto1.velocidad_actual}")

auto1.frenar()
print(f"Velocidad actual = {auto1.velocidad_actual}")

auto1.desacelerar(20)