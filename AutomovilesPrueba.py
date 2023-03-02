"""Prueba"""
class automoviles():
    def __init__(self, motor, marca, modelo):
        self.motor = motor
        self.marca = marca
        self.modelo = modelo
        self.arrancado = False

    def arrancar(self):
        if self.arrancado == True:
            print("Estoy arrancado")
        else:
            print("Estoy arrancando")
            self.arrancando = True

    def parar(self):
        if self.arrancado == False:
            print("Estoy parado")
        else:
            print("Estoy parando")



