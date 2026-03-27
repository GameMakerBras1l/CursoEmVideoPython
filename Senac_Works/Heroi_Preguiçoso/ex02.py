class Produto:
    def __init__ (self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__ (self):
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def calcular_total(self):

        total = 0

        for produto in self.itens:
            total = total + produto.preco

        return total
    
p1 = Produto("Mouse", 50)
p2 = Produto("Teclado", 100)
p3 = Produto("Monitor", 800)

carrinho = Carrinho()

carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)
carrinho.adicionar_produto(p3)

print("Total da compra:", carrinho.calcular_total())