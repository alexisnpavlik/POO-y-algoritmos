class Animal:

    def __init__(self,especie,edad):
        self.especie = especie
        self.edad = edad

    def describe(self):
        print("Soy un Animal del tipo", type(self).__name__)

# creamos una clase que hereda los atributos de la anteriores
class Perro(Animal):
    pass

print(Perro.__bases__) #Para saber su clase padre
print(Animal.__subclasses__()) #Para saber su clase hijo

#creamos una instancia con atributos del padre
mi_perro=Perro("canino",18)

#Usamos metodos del padre
mi_perro.describe()

#Imprimimos una pupla con la herencia de la clase
print(Perro.__mro__) 

