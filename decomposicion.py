class Automovil:

    def __init__(self,motor,modelo,marca,color,deportivo=False): #default keyword
        self.motor = motor
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self.deportivo = deportivo
        self._estado="en_reposo" #atributo privado que no es visible para quienes usen las clases
        self._motor= Motor(cilindros=4)

class Motor:
    
    def __init__(self,cilindros,tipo="gasolina"):
        self.cilindros=cilindros
        self.tipo=tipo
        self._temperatura=0
    
    def injecta_gasolina(self,cantidad):
        pass

    def acelerar(self,tipo="lento"):
        if tipo == "rapido":
            self.injecta_gasolina(10) #Self para modificar un atributo
        else:
            self.injecta_gasolina(5)
        
        self._estado="en_movimiento"