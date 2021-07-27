class coordenada:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distancia(self,otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff+y_diff)**(1/2)
    
def run():
    coor_1=coordenada(3,30)
    coor_2=coordenada(2,15)

    #print(coor_1.distancia(coor_2))
    print(isinstance(coor_1,coordenada))

if __name__=='__main__':
    run()