class Veiculo:

    def __init__(self,color,wheels):
        self.color = color
        self.wheels = wheels
    
class Car(Veiculo):
    
    def __init__(self,color,wheels,velocity,cilidrada):
        self.color=color
        self.wheels=wheels
        self.velocity = velocity
        self.cilidrada =cilidrada

    def __str__(self):
        return f"El veiculo es de color {self.color}, tiene {self.wheels} ruedas. Tiene un motor de {self.cilidrada} cilindrada y alcanza un velocidad de {self.velocity} km/h"

auto_1=Car("red",4,40,4.3)
print(auto_1)

#Ahora si no queremos volver a inicalizar las variables en la clase hija lo que podemos hacer es usar un pequño truco

class Car():
    def __init__(self,color,wheels,velocity,cilidrada):
        Veiculo.__init__(self,color,wheels)
        self.velocity= velocity
        self.cilidrada=cilidrada
     
    def __str__(self):
        return f"El veiculo es de color {self.color}, tiene {self.wheels} ruedas. Tiene un motor de {self.cilidrada} cilindrada y alcanza un velocidad de {self.velocity} km/h"

auto_1=Car("red",4,40,4.3)
print(auto_1)