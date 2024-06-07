class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
class Maestro(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado=grado
class Estudiante(Persona):
    def __init__(self, nombre, edad, codigo):
        super().__init__(nombre, edad)
        self.codigo=codigo
class Universitario(Estudiante):
    def __init__(self, nombre, edad, codigo, carrera):
        super().__init__(nombre, edad, codigo)
        self.carrera=carrera

u1=Universitario("Carlos",23,"02324","sistemas")
print(u1.carrera)