import random

frases = ["Presença de vida detectada", "Planeta inóspito", "Recursos minerais encontrados"]

class ModuloEscudo:

    def __init__(self, energia):
        self.energia = energia

class NaveEspacial:

    def __init__ (self, nome, tripulacao, integridade_casco):
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
                energia = self.escudo.energia
                dano = dano - self.escudo.energia
                self.escudo.energia = 0
                self.integridade_casco -= dano
        else:
            self.integridade_casco -= dano


        if self.integridade_casco < 0:
            self.integridade_casco = 0
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
        scan = random.choice(frases)

        return scan
    
def relatorio_inspecao(lista_naves):

    for nave in lista_naves:
        nave.nome
        nave.integridade_casco