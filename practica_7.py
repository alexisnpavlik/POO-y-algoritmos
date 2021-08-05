class Calculadora:
    

    def __init__(self,number_1,number_2):
        self.number_1 = number_1
        self.number_2 = number_2
    
    def suma(self):
        print(f"La suma es: {self.number_1 + self.number_2}")
    
    def resta(self):
        print(f"La resta es: {self.number_1 - self.number_2}")
    
    def multiplicacion(self):
        print(f"La multiplicacion es: {self.number_1 * self.number_2}")
    
    def divicion(self):
        print(f"La divicion es: {self.number_1 / self.number_2}")
    
numeritos=Calculadora(2,3)
numeritos.suma()
numeritos.resta()
numeritos.multiplicacion()
numeritos.divicion()
