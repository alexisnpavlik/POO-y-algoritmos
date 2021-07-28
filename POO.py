#Definimos una clase
class Hotel:
#definimos los atributos 
    def __init__(self,numero_maximo_huespedes,lugares_de_estacionamiento): #Generamos una instancia llamando al constructor de clase
        self.numero_maximo_huespedes = numero_maximo_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0 #inicialixamos las variables


hotel=Hotel(numero_maximo_huespedes=50, lugares_de_estacionamiento=20) 
#creamos una instancia "hotel" con el molde "Hotel"
print(hotel.lugares_de_estacionamiento)

class Hotel:
    #definimos los metodos
    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes): #huespedes se van
        self.huespedes -= cantidad_de_huespedes
        
    def ocupacion_total(self):
        return self.huespedes


hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
hotel.checkout(1)
hotel.ocupacion_total() 
