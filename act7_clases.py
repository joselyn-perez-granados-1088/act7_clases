print("INTRODUCCION A CLASES")
class animal:
    edad=3
    raza="pitbull"
    comida="croquetas"
    def come(self):
        print(f"el perro come "+self.comida)
print(animal)
print("creando el objeto de la clase josy")
perre=animal()
print(f"edad de animal {perre.edad}")
print(f"raza de animal {perre.raza}")
lacomida=perre.come()
