# mtg_duel.py
# 🕹️ Scenario 03: The Combat Logic
# Objective: Handle interaction between two different instances.

class Creature:
    def __init__(self, name, power, toughness):
        self.name = name
        self.power = power
        self.toughness = toughness
        self.is_alive = True

    def attack(self, target):
        if not self.is_alive:
            print(f"[!] {self.name} is dead and cannot attack!")
            return

        print(f"⚔️ {self.name} attacks {target.name} for {self.power} damage!")
        target.take_damage(self.power)

    def take_damage(self, amount):
        self.toughness -= amount
        print(f"🛡️ {self.name} received {amount} damage. Remaining Toughness: {self.toughness}")
        if self.toughness <= 0:
            self.die()

    def die(self):
        self.is_alive = False
        print(f"💀 {self.name} has been destroyed!")

if __name__ == "__main__":
    # Instantiate two classic MTG creatures
    bears = Creature("Grizzly Bears", 2, 2)
    goblin = Creature("Raging Goblin", 1, 1)

    print("--- THE DUEL BEGINS ---")
    goblin.attack(bears)
    bears.attack(goblin)
