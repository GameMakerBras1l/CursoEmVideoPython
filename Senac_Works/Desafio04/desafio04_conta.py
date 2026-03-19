class ContaCorrente:
    def __init__(self, saldo):
        self.saldo = saldo

    def transferir(self, destino, valor):

        if self.saldo >= valor > 0:
            self.saldo -= valor
            destino.saldo += valor

        else:
            print("Erro")

a = ContaCorrente(1000)
b = ContaCorrente(500)

a.transferir(b, 200)
print(a.saldo)
print(b.saldo)