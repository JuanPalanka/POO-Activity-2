class Persona:
    def __init__(self, nombre, apellido, numero_documento_identidad, ano_nacimiento, pais_nacimiento, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_documento_identidad = numero_documento_identidad
        self.ano_nacimiento = ano_nacimiento
        self.pais_nacimiento = pais_nacimiento
        self.genero = genero
    def imprimir(self):
        print(f"Nombre= {self.nombre}")
        print(f"Apellido= {self.apellido}")
        print(f"Numero de documento de identidad= {self.numero_documento_identidad}")
        print(f"Ano de nacimiento= {self.ano_nacimiento}")
        print(f"Pais de Nacimiento= {self.pais_nacimiento}")
        print(f"Genero= {self.genero}")


p1 = Persona("Pedro", "Perez", "1053121010", 1998, "Colombia", "H")
p2 = Persona("Diana", "Soto", "1053223344", 2001, "Argentina", "M")

p1.imprimir()
p2.imprimir()