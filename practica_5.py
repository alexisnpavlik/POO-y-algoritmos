class Alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def evaluacion(self):
        if self.nota >= 6:
            print(f"El alumno {self.nombre} aprobo")
            print(f"Consiguio una nota de {self.nota}")
        else:
            print(f"El alumno {self.nombre} no aprobo")

alumno_1=Alumno("alexis",8)

alumno_1.evaluacion()