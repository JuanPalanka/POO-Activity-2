from enum import Enum


class Tipo(Enum):
    AHORROS = "AHORROS"
    CORRIENTE = "CORRIENTE"


class CuentaBancaria:
    def __init__(self, nombres_titular: str, apellidos_titular: str, numero_cuenta: int, tipo_cuenta: Tipo):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = 0.0
        self.interes= 0.2

    def imprimir(self) -> None:
        print(f"Nombres del titular = {self.nombres_titular}")
        print(f"Apellidos del titular = {self.apellidos_titular}")
        print(f"Número de cuenta = {self.numero_cuenta}")
        print(f"Tipo de cuenta = {self.tipo_cuenta.name}")
        print(f"Saldo = {self.saldo}")

    def consultar_saldo(self) -> None:
        print(f"El saldo actual es = {self.saldo}")

    def consignar(self, valor: int) -> bool:
        if valor > 0:
            self.saldo = self.saldo + valor
            print(f"Se ha consignado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor: int) -> bool:
        if valor > 0 and valor <= self.saldo:
            self.saldo = self.saldo - valor
            print(f"Se ha retirado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        else:
            print("El valor a retirar debe ser menor que el saldo actual.")
            return False

    def intereses(self):
        self.saldo= self.saldo- (self.saldo*self.interes)
        print(f"Despues de intereses, el nuevo saldo es: ${self.saldo}")


cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, Tipo.AHORROS)
cuenta.imprimir()
cuenta.consignar(200000)
cuenta.consignar(300000)
cuenta.retirar(400000)
cuenta.intereses()