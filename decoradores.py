
def decorador(funcion_parametro):
    def funcion_interior():
        print("Agrega texto")
        funcion_parametro()
        print("terminado")
    return funcion_interior()

@decorador
def suma():
    print(5+8)