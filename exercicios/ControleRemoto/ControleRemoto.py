from abc import ABC,abstractmethod

class ControleRemoto:
    def __init__(self, volume=50, ligado=False, tocando=False):
        self.__volume = volume
        self.__ligado = ligado
        self.__tocando = tocando

    # métodos abstratos
    @abstractmethod
    def ligar(self):
        self.Setligado(True)

    @abstractmethod
    def desligar(self):
        self.Setligado(False)
        self.Settocando(False)

    @abstractmethod
    def abrirMenu(self):
        print('<<<<<< MENU >>>>>>')
        print(f'Está ligado ? {self.Getligado()}')
        print(f'Está tocando ? {self.Gettocando()}')
        print(f'Volume: {self.Getvolume()}')
        for v in range(0, self.Getvolume(),10):
            print('| ', end='')

    @abstractmethod
    def fecharMenu(self):
        print('\n[ Fechando Menu ... ]')

    @abstractmethod
    def maisVolume(self):
        if self.Getligado() == True:
            self.Setvolume(5) 
        else:
            print('Error! Impossível aumentar volume, verifique se seu aparelho está ligado.')

    @abstractmethod
    def menosVolume(self):
        if self.Getligado() == True:
            self.Setvolume(- 5)
        else:
            print('Error! Impossível diminuir volume, verifique se seu aparelho está ligado.')

    @abstractmethod
    def ligarMudo(self):
        if self.Getvolume() and self.Getligado() > 0:
            self.Setvolume(0) 

    @abstractmethod
    def desligarMudo(self):
        if self.Getvolume() and self.Getligado() == 0:
            self.Setvolume(50)

    @abstractmethod
    def play(self):
        if self.Getligado() and self.Gettocando() == False:
            self.Settocando(True)
        else:
            print('Error! verifique se seu aparelho está ligado.')

    @abstractmethod   
    def pause(self):
        if self.Getligado() and self.Gettocando() == True:
            self.Settocando(False)  
        else:
            print('Error! verifique se seu aparelho está ligado.') 

    # métodos especiais 
    def Getvolume(self):
        return self.__volume

    def Setvolume(self, v):
        if v < 0:
            self.__volume += v
        else:
            self.__volume -= v

    def Getligado(self):
        return self.__ligado

    def Setligado(self, l):
        self.__ligado = l

    def Gettocando(self):
        return self.__tocando

    def Settocando(self, t):
        self.__tocando = t