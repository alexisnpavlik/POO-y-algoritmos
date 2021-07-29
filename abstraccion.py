class Lavadora:

    def __init__(self):
        pass

    def lavar(self,temperatura='caliente'):
        self.llenar_tanque(temperatura)
        self.añadir_jabon()
        self.centrifugar()

    def llenar_tanque(self,temperatura):
        print(f"llenando el tanque con agua {temperatura}")
    
    def añadir_jabon(self):
        print(f"añadiendo jabon")

    def centrifugar(self):
        print("Ahi te voy perro")

def run():
    lavadora=Lavadora()
    lavadora.lavar()

if __name__=='__main__':
    run()