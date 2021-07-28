class Persona:
    def __init__(self,altura,peso,genero,edad,nombre):
        self.altura = altura
        self.peso = peso
        self.genero = genero
        self.edad = edad
        self.nombre = nombre
    
    #definimos algunos metodos
    def hablar(self):
        print("Hola soy {}".format(self.nombre))
    
    def correr(self):
        print("{} esta corriendo".format(self.nombre))

#creamos instancias

persona1 =Persona(178,67,"M",18,"alexis")
persona2 =Persona(163,68,"F",24,"rocio")


def run():
    print(persona1.hablar())
    
if __name__=='__main__':
    run()