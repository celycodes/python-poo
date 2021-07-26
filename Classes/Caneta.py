class Caneta:
    def __init__(self, modelo, cor, ponta, carga, tampada):
        self.modelo = modelo
        self.cor = cor
        self.ponta = ponta
        self.carga = carga
        self.tampada = tampada

    def rabiscar(self):
        if self.tampada is True:
            print('Error ! não é possivel rabiscar a caneta está tampada ...')
        else:
            print('<<< Estou Rabiscando >>>')

    def tampar(self):
        self.tampada = True

    def destanpar(self):
        self.tampada = False

    def __str__(self):
        print('-='*15)
        return f'Modelo: {self.modelo}\nCor: {self.cor}\nPonta: {self.ponta}\nCarga: {self.carga}\nTampada: {self.tampada}'