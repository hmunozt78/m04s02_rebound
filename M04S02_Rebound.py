class Animal:
    def __init__(self, nombre:str, edad:int, raza:str, peso:int) -> None:
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
    
    def informar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad}. \nMi Raza es {self.raza} y peso {self.peso} Kgs \n \n"
    
caballo = Animal("Zeus", 5, "Pura Sangre", 450)
leon = Animal("Boulder", 10, "Atlas", 130)

print(caballo.informar())
print(leon.informar())