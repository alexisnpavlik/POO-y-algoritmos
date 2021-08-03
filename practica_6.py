class Triangulo:
    def __init__(self):
        self.lado_1=int(input("Ingrese el lado 1: "))
        self.lado_2=int(input("Ingrese el lado 2: "))
        self.lado_3=int(input("Ingrese el lado 3: "))
    
    def imprimir(self):
        print("Lado 1 :",self.lado_1)
        print("Lado 2 :",self.lado_2)
        print("Lado 3 :",self.lado_3)

    def mayor(self):
        lado_mayor=max(self.lado_1, self.lado_2, self.lado_3)
        if lado_mayor==self.lado_1:
            print("El Lado 1 es el mayor")
        elif lado_mayor==self.lado_2:
            print("El Lado 2 es el mayor")
        elif lado_mayor==self.lado_3:
            print("El Lado 3 es el mayor")
    

    def tipo_trianulo(self):
        if self.lado_1==self.lado_2 and self.lado_2==self.lado_3:
            print("Se trata de un triangulo Equilatero")
        elif self.lado_1==self.lado_2 or self.lado_2==self.lado_3 or self.lado_3==self.lado_1:
            print("Se trata de un triangulo Isoceles")
        else:
            print("Se trata de un triangulo Escaleno")

poligono_3_lados=Triangulo()
poligono_3_lados.imprimir()
poligono_3_lados.mayor()
poligono_3_lados.tipo_trianulo()
