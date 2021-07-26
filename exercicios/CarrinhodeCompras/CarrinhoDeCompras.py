class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(f'Produto: {produto.nome} Valor: R${produto.valor}')

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total