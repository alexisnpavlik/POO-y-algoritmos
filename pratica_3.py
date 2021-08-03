class Veiculo:

    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas =ruedas

class Coche(Veiculo):
    def __init__(self,color,ruedas,velocidad,cilidrada):
        Veiculo.__init__(self,color,ruedas)
        self.velocidad= velocidad
        self.cilidrada=cilidrada
    
class Camioneta(Coche):
    def __init__(self,color,ruedas,velocity,cilidrada,carga):
        Coche.__init__(self,color,ruedas,velocity,cilidrada)
        self.carga=carga
    
class Bicicleta(Veiculo):
    def __init__(self,color,ruedas,tipo="urbana"):
        Veiculo.__init__(self,color,ruedas)
        self.tipo=tipo
    
class Motocicleta(Bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad,cilidrada):
        Bicicleta.__init__(self,color,ruedas,tipo)
        self.velocidad=velocidad
        self.cilidrada=cilidrada


