class Agenda:
    
    def __init__(self):
        self.contactos=[] 

    def Menu(self):
        print()
        menu = [
            ['Agenda Personal'],
			['1. Añadir Contacto',"anadir"],
			['2. Lista de contactos'],
			['3. Buscar contacto'],
			['4. Editar contacto'],
			['5. Cerrar agenda']
        ]

        for i in range(6):
            print(menu[i])

agenda=Agenda()
agenda.Menu()