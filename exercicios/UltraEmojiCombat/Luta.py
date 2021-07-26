from random import randint
import Lutador
class luta:
    def __init__(self, desafiado, desafiante, rounds, aprovada):
        self.__desafiado = Lutador
        self.__desafiante = Lutador
        self.__rounds = rounds
        self.__aprovada = aprovada

    def marcarLuta(self, l1, l2):
        if (l1.Getcategoria() == l2.Getcategoria()) and l1 != l2:
            self.__aprovada = True
            self.__desafiado = l1
            self.__desafiante = l2
        else:
            self.__aprovada = False
            self.__desafiado = None
            self.__desafiante = None
    def lutar(self):
        if self.__aprovada is True:
            print('------------ DESAFIADO ------------')
            self.__desafiado.apresentar()
            print('------------ DESAFIANTE ------------')
            self.__desafiante.apresentar()
            vencedor = randint(0, 2)
            print('-------- Resultado da Luta --------')
            if vencedor == 0: #empate
                print('Empatou!')
                self.__desafiado.empatar()
                self.__desafiante.empatar()
            elif vencedor == 1: # desadiado vence
                print(f'Vitória do {self.__desafiado.Getnome()}')
                self.__desafiado.ganharLuta()
                self.__desafiante.perderLuta()
            elif vencedor == 2: # desafiante vence
                print(f'Vitória do {self.__desafiante.Getnome()}')
                self.__desafiante.ganharLuta()
                self.__desafiado.perderLuta()
        else:
            print('A luta não pode acontecer!')
        print('-' * 35)
