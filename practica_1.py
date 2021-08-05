class Perro():

    def __init__(self, name,age):
        self.name = name
        self.age = age
    def ladrar():
        print("Wau")

    def __str__(self):
        return f"{self.name} de {self.age} años"

perro_1=Perro("bobi",21)
print (perro_1)
