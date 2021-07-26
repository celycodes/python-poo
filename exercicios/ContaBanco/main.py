import ContaBanco 

conta1 = ContaBanco.ContaBanco(1,'CC','Celenny Cristhyne', 100, True)
conta1.abrirconta()
print(conta1)
conta1.fecharconta()

'''
Instanciando um objeto conta1 com o uso da classe ContaBanco
 * Tipo
   - CC = conta corrente 
   - CP = conta poupança
 * Status 
   - False = Conta fechada
   - True  = Conta Aberta
'''