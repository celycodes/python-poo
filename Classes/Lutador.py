class Lutador:
    def __init__(self, nome, nacionalidade, idade, altura, peso, vitorias, derrotas, empates):
        self.__nome = nome
        self.__nacionalidade = nacionalidade
        self.__idade = idade
        self.__altura = altura
        self.__peso = peso
        self.__categoria = ''
        self.__vitorias = vitorias
        self.__derrotas = derrotas
        self.__empates = empates

    def apresentar(self):
        print(f'<<<< INFORMAÇÕES >>>>\nNome: {self.Getnome()}\nNacionalidade: {self.Getnacionalidade()}\nIdade: {self.Getidade()}\nPeso: {self.Getpeso()} Kg')

    def status(self):
        print(f'<<<<  STATUS  >>>>\nNome: {self.Getnome()}\nCategoria: {self.Getcategoria()}\nVitórias: {self.Getvitorias()}\nDerrotas: {self.Getderrotas()}\nEmpates: {self.Getempates()}\n')

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
        self.Getcategoria()

    def Getcategoria(self):
        return self.__categoria

    def Setcategoria(self):
        if self.__peso <= 52.2:
            self.__categoria = 'Inválido'
        elif self.__peso >= 52.3 and self.__peso <= 70.3:
            self.__categoria = 'Leve'
        elif self.__peso > 70.3 and self.__peso <= 83.9:
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