# mtg_duel.py
# 🕹️ Scenario 03: The Combat Logic (Refatorado)
# Objective: Melhorar a integridade do sistema de combate

class Creature:
    # Classe que representa uma criatura no estilo MTG

    def __init__(self, name, power, toughness):
        self.name = name
        # Nome da criatura

        self._power = power
        # Atributo "protegido" (convenção) para poder

        self._toughness = toughness
        # Atributo "protegido" para resistência

        self.is_alive = True
        # Indica se a criatura está viva

    # =========================
    # 🔹 PROPERTY: POWER
    # =========================
    @property
    def power(self):
        # Getter do poder
        return self._power

    @power.setter
    def power(self, value):
        # Setter com validação
        if value < 0:
            raise ValueError("Power não pode ser negativo!")
        self._power = value

    # =========================
    # 🔹 PROPERTY: TOUGHNESS
    # =========================
    @property
    def toughness(self):
        # Getter da resistência
        return self._toughness

    @toughness.setter
    def toughness(self, value):
        # Setter com validação
        if value < 0:
            raise ValueError("Toughness não pode ser negativo!")
        self._toughness = value

    # =========================
    # 🔹 COMBATE SIMULTÂNEO
    # =========================
    def fight(self, opponent):
        # Método que representa combate simultâneo (estilo MTG)

        if not self.is_alive or not opponent.is_alive:
            print("[!] Uma das criaturas está morta e não pode lutar!")
            return

        print(f"\n⚔️ {self.name} VS {opponent.name} ⚔️")

        # 🔬 Forense de memória
        print(f"id(self): {id(self)}")
        print(f"id(opponent): {id(opponent)}")

        # Dano simultâneo (armazenado antes de aplicar)
        damage_to_opponent = self.power
        damage_to_self = opponent.power

        # Aplicação simultânea
        opponent.toughness -= damage_to_opponent
        self.toughness -= damage_to_self

        print(f"{self.name} ficou com {self.toughness} de toughness")
        print(f"{opponent.name} ficou com {opponent.toughness} de toughness")

        # Verifica mortes
        if self.toughness <= 0:
            self.die()

        if opponent.toughness <= 0:
            opponent.die()

    def die(self):
        # Método de morte
        self.is_alive = False
        print(f"💀 {self.name} foi destruído!")


# =========================
# 🔹 TESTE DO SISTEMA
# =========================
if __name__ == "__main__":
    c1 = Creature("Grizzly Bears", 2, 2)
    c2 = Creature("Raging Goblin", 1, 1)

    print("--- COMBATE SIMULTÂNEO ---")
    c1.fight(c2)