class saludo():
    def __init__(self,mensaje):
        self.mensaje = mensaje

    def saludar (self):
        print(self.mensaje)

saludo = saludo("hola mundo")
saludo.saludar()