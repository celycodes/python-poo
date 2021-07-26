class ContaBanco:
    def __init__(self, numconta, tipo, dono, saldo, status):
       self.numconta = numconta
       self.tipo = tipo
       self.dono = dono
       self.saldo = saldo
       self.status = status 

    def abrirconta(self):
        while self.tipo not in 'CCP':
            if self.tipo == 'CC':
                self.saldo += 50
            else:
                self.saldo += 150
        self.status = True

    def fecharconta(self):
        if self.saldo > 0:
            print('Oops! Você ainda tem saldo essa operação é indisponível.')
        elif self.saldo < 0:
            print('Error! Seu saldo está negativo impossível efetuar a operação.')
        else:
            print('Operação efetuada com sucesso ...')
            self.status = False

    def depositar(self,valor):
        if self.status is True:
            self.saldo += valor

    def sacar(self,valorsaque):
        if self.status is True:
            if self.saldo >= valorsaque:
                self.saldo -= valorsaque
            else:
                return f'Error! Saldo insuficiente ...'

    def pagarmensal(self):
        if self.saldo >= 12 and self.saldo <= 20:
            if self.tipo == 'CC':
                self.saldo -= 12
            else:
                self.saldo -= 20
        else:
            return 'Error! Saldo insuficiente ...'

    def __str__(self):
        return f'Dono: {self.dono}\nID: {self.numconta}\nTipo: {self.tipo}\nStatus: {self.status}\nSaldo: R${self.saldo:.2f}'