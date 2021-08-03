class Cuadrilatero:
    def __init__(self,lados):
        self.lados =lados
        self.suma_lados=360

    def perimetro(self):
        return sum(self.suma_lados)

    def __str__(self):
        return self.perimetro   

cuadrado_1=Cuadrilatero([2,3,4,5])

print(cuadrado_1.perimetro)