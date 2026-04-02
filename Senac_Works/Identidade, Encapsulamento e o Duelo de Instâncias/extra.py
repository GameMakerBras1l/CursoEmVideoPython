class Criatura:
    def __init__(self, nome, poder, resistencia):
        self.nome = nome
        self.poder = poder
        self.resistencia = resistencia

    def atk(self):
        print(f"{self.nome} realiza um ataque básico!")

class Dragao(Criatura):
    # HERANÇA: Dragao herda de Criatura

    def atk(self):
        # POLIMOFISMO
        super().atk()
        print(f"{self.nome} respiração de fogo.")

class Kitsune(Criatura):
    # Raposa mitica do flocore japones, ganha uma
    # nova cauda a cada ceculo até atigir o numero 9
    def atk(self):
        super().atk()
        print(f"{self.nome} magia de fogo.")


if __name__ == "__main__":
    criaturas = [
        Dragao ("Dragão Celeste", 5, 5),
        Kitsune ("Nove Caudas", 5, 3)
    ]

    for c in criaturas:
        c.atk()

# O polimorfismo ocorre quando diferentes classes sobrescrevem um
# mesmo método (atk), apresentando comportamentos distintos. O uso
# de super() permite reutilizar o comportamento da classe base,
# adicionando funcionalidades específicas em cada subclasse.

# Obs: criado separado dos outro codigos para ficar mais organizado.