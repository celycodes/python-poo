import CarrinhoDeCompras as car
import Produto as pro

carrinho = car.CarrinhoDeCompras()
p1 = pro.Produto('Caneca', 15)
p2 = pro.Produto('Camisa', 45)
p3 = pro.Produto('Iphone', 10000)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.lista_produto()

'''
Exemplo disponivel no canal do YouTube Ótavio Miranda
* Agregação - Python Orientado a Objetos - Aula 42
'''