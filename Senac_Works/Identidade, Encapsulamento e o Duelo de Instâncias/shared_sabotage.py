# shared_sabotage.py
# 🕹️ Scenario 02: The Sabotage of Shared State
# Objective: The "Ghost" Inventory.

class Fighter:
    # Define a classe Fighter/Lutador

    # SABOTAGE: Using Class Attribute for Instance Data
    # Every Fighter will share the SAME memory address for this list.
    inventory = []
    # ERRO: inventory é um atributo de CLASSE
    # Isso significa que TODOS os objetos Fighter compartilham a mesma lista

    def __init__(self, name):
        # Método construtor chamado ao criar um novo objeto

        self.name = name
        # Armazena o nome do Lutador no objeto

    def pick_item(self, item):
        # Método para adicionar um item ao inventário

        self.inventory.append(item)
        # Adiciona o item na lista inventory
        # Como inventory é compartilhado, todos os objetos são afetados

        print(f"{self.name} picked up: {item}")
        # Exibe mensagem informando o item coletado


if __name__ == "__main__":
    # Garante que o código abaixo só roda se o arquivo for executado diretamente

    f1 = Fighter("Scorpion")
    # Cria o primeiro Lutador chamado Scorpion

    f2 = Fighter("Sub-Zero")
    # Cria o segundo Lutador chamado Sub-Zero

    print(f"--- F1 starts: {f1.name} ---")
    # Exibe mensagem inicial para o primeiro Lutador

    f1.pick_item("Spear")
    # Scorpion pega uma lança
    # Isso adiciona o item no inventory COMPARTILHADO

    print(f"\n--- F2 starts: {f2.name} ---")
    # Início do segundo Lutador

    print(f"Inventory of {f2.name}: {f2.inventory}")
    # Aqui aparece o erro:
    # Sub-Zero já tem "lança" mesmo sem ter pegado nada

    print("[?] How did he get a spear?! He just spawned!")
    # Mensagem destacando o bug

    f2.pick_item("Ice Bomb")
    # Sub-Zero pega outro item
    # Esse item também vai para o MESMO inventory compartilhado

    print(f"\nInventory of {f1.name}: {f1.inventory}")
    # Agora Scorpion também vê o item do Sub-Zero

    print("[!] The state is leaked! Every instance is bleeding into the other.")
    # Mensagem final explicando o problema:
    # vazamento de estado entre objetos

    # O erro ocorre porque o atributo inventory foi definido como atributo de classe,
    # fazendo com que todas as instâncias compartilhem a mesma referência em memória.
    # Como listas são mutáveis, qualquer modificação feita por um objeto afeta os demais,
    # causando vazamento de estado.