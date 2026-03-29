import random

frases = [
    "Presença de vida detectada",
    "Planeta inóspito",
    "Recursos minerais encontrados"
]

class ModuloEscudo:

    def __init__(self, energia):
        self.energia = energia


class NaveEspacial:

    def __init__(self, nome, tripulacao, integridade_casco):
        self.nome = nome
        self.tripulacao = tripulacao
        self.integridade_casco = integridade_casco
        self.escudo = None

    def viajar(self, anos_luz):
        self.integridade_casco -= anos_luz

        if self.integridade_casco < 0:
            self.integridade_casco = 0

    def sofrer_ataque(self, dano):

        if self.escudo is not None:

            if dano <= self.escudo.energia:
                self.escudo.energia -= dano

            else:
                dano_restante = dano - self.escudo.energia
                self.escudo.energia = 0
                self.integridade_casco -= dano_restante

        else:
            self.integridade_casco -= dano

        if self.integridade_casco < 0:
            self.integridade_casco = 0

    def atacar(self, outra_nave):
        dano = random.randint(10, 100)
        print(f"{self.nome} atacou {outra_nave.nome} causando {dano} de dano!")
        outra_nave.sofrer_ataque(dano)


class NaveCargueiro(NaveEspacial):

    def __init__(self, nome, tripulacao, integridade_casco, capacidade_carga):
        super().__init__(nome, tripulacao, integridade_casco)
        self.capacidade_carga = capacidade_carga
        self.carga_atual = 0

    def carregar(self, toneladas):

        if self.carga_atual + toneladas <= self.capacidade_carga:
            self.carga_atual += toneladas
            print("Carga adicionada com sucesso")
        else:
            print("Não é possível adicionar mais carga")


class NaveExploradora(NaveEspacial):

    def __init__(self, nome, tripulacao, integridade_casco, sensores):
        super().__init__(nome, tripulacao, integridade_casco)
        self.sensores = sensores

    def escanear_planeta(self):
        resultado = random.choice(frases)
        print(f"{self.nome} escaneou o planeta: {resultado}")
        return resultado


def relatorio_inspecao(lista_naves):

    print("\n=== RELATÓRIO DAS NAVES ===")

    for nave in lista_naves:

        escudo_status = (
            f"{nave.escudo.energia}" if nave.escudo is not None else "Sem escudo"
        )

        print(f"Nave: {nave.nome}")
        print(f"Tripulação: {nave.tripulacao}")
        print(f"Integridade do casco: {nave.integridade_casco}")
        print(f"Escudo: {escudo_status}")
        print("-" * 30)


# =========================
# TESTE DO SISTEMA
# =========================

nave1 = NaveEspacial("Enterprise", 100, 500)
nave2 = NaveCargueiro("CargoX", 50, 300, 1000)
nave3 = NaveExploradora("Explorer", 20, 200, "Avançados")

# adicionando escudos
nave1.escudo = ModuloEscudo(100)
nave3.escudo = ModuloEscudo(50)

# ações iniciais
nave2.carregar(500)
nave3.escanear_planeta()

# batalha
print("\n=== BATALHA ===")
nave1.atacar(nave3)
nave3.atacar(nave1)
nave2.atacar(nave1)

# relatório final
lista = [nave1, nave2, nave3]
relatorio_inspecao(lista)