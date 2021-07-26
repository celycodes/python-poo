class Lutador:
    def __init__(self, nome, nacionalidade, idade, altura, peso, vitorias, derrotas, empates):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__idade = idade
        self.__altura = altura
        self.__peso = peso
        self.__categoria = None
        self.__vitorias = vitorias
        self.__derrotas = derrotas
        self.__empates = empates

    def apresentar(self):
        print(f'Apresentamos o lutador {self.Getnome()}\nDiretamente de {self.Getnacionalidade()}, com {self.Getidade()} anos\nPesando {self.Getpeso()} Kg e com {self.Getaltura()} de altura')
        print(f'{self.Getvitorias()} vitórias | {self.Getderrotas()} derrotas | {self.Getempates()} empates ! ')

    def status(self):
        self.Setcategoria()
        print(f'{self.Getnome()} é um peso {self.Getcategoria()}\nGanhou {self.Getvitorias()} vezes\nPerdeu {self.Getderrotas()} vezes\nEmpatou {self.Getempates()} vezes')
        print('-' * 35)

    def ganharLuta(self):
        self.Setvitorias(self.__vitorias + 1)

    def perderLuta(self):
        self.Setderrotas(self.__derrotas + 1)

    def empatar(self):
        self.Setempates(self.__empates + 1)

    #metodos especiais 
    def Getnome(self):
        return self.__nome

    def Setnome(self, no):
        self.__nome = no

    def Getnacionalidade(self):
        return self.__nacionalidade 

    def Setnacionalidade(self, na):
        self.__nacionalidade = na

    def Getidade(self):
        return self.__idade

    def Setidade(self, id):
        self.__idade = id

    def Getaltura(self):
        return self.__altura

    def Setaltura(self, al):
        self.__altura = al

    def Getpeso(self):
        return self.__peso

    def Setpeso(self, pe):
        self.__peso = pe
        self.Setcategoria()

    def Getcategoria(self):
        self.Setcategoria()
        return self.__categoria

    def Setcategoria(self):
        peso = self.__peso
        if peso <= 52.2:
            self.__categoria = 'Inválido'
        elif peso > 52.2 and peso <= 70.3:
            self.__categoria = 'Leve'
        elif peso > 70.3 and peso <= 83.9:
            self.__categoria = 'Médio'
        else:
            self.__categoria = 'Pesado'

    def Getvitorias(self):
        return self.__vitorias

    def Setvitorias(self, vi):
        self.__vitorias = vi

    def Getderrotas(self):
        return self.__derrotas

    def Setderrotas(self, de):
        self.__derrotas = de   

    def Getempates(self):
        return self.__empates

    def Setempates(self, em):
        self.__empates = em

