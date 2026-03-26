class Personagem:
    def __init__ (self, nome, classe, hp_max):
        self.nome = nome
        self.classe = classe
        self.hp_max = hp_max

        self.nivel = 1
        self.hp_atual = hp_max

    def receber_dano(self, quantidade):

        self.hp_atual = self.hp_atual - quantidade

        if self.hp_atual < 0:
            self.hp_atual = 0

    def curar(self, quantidade):

        self.hp_atual = self.hp_atual + quantidade

        if self.hp_atual > self.hp_max:
            self.hp_atual = self.hp_max

    def subir_nivel(self):

        self.nivel = self.nivel + 1

        self.hp_max = self.hp_max + (self.hp_max/10)
        self.hp_atual = self.hp_max

    

p1 = Personagem("Aragorn", "Paladino", 100)

print("Status inicial:")
print("Nome: ", p1.nome, "Classe: ", p1.classe, "Nivel: ", p1.nivel, "||", p1.hp_atual, "/", p1.hp_max)

print("\nRecebeu dano de 30:")
p1.receber_dano(30)
print("Nome: ", p1.nome, "Classe: ", p1.classe, "Nivel: ", p1.nivel, "||", p1.hp_atual, "/", p1.hp_max)

print("\nCurou 20:")
p1.curar(20)
print("Nome: ", p1.nome, "Classe: ", p1.classe, "Nivel: ", p1.nivel, "||", p1.hp_atual, "/", p1.hp_max)

print("\nSubiu de nível:")
p1.subir_nivel()
print("Nome: ", p1.nome, "Classe: ", p1.classe, "Nivel: ", p1.nivel, "||", p1.hp_atual, "/", p1.hp_max)
