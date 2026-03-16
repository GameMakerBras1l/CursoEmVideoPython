"""
MEET 02: O PROBLEMA DO DIA (ADS Edition)
Tópico: A Fragilidade do Estado Global e Identidade por Índice
Instrução Hypatia: "Sinta a dor antes de buscar a cura."
"""


titulares = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
saldos = [1500.0, 2500.0, 500.0, 3000.0, 100.0, 4500.0]
tipos = ["GOLD", "STANDARD", "STANDARD", "GOLD", "STANDARD", "GOLD"]


transacoes = [
    {"de": 0, "para": 1, "valor": 200.0},
    {"de": 3, "para": 2, "valor": 150.0},
    {"de": 5, "para": 4, "valor": 50.0}
]

def adicionar_conta(nome, saldo_inicial, tipo="STANDARD"):
    """Adiciona uma nova conta ao final das listas."""
    titulares.append(nome)
    saldos.append(saldo_inicial)
    tipos.append(tipo)
    print(f"[OK] Conta de {nome} criada no índice {len(titulares)-1}")

def remover_conta(indice):
    """Remove uma conta e ajusta as listas. CUIDADO: Isso altera todos os índices posteriores!"""
    nome = titulares.pop(indice)
    saldos.pop(indice)
    tipos.pop(indice)
    print(f"[ALERTA] Conta de {nome} (Índice {indice}) removida do sistema.")

def transferir(indice_origem, indice_destino, valor):
    """Realiza transferência entre contas via índice."""
    if saldos[indice_origem] >= valor:
        saldos[indice_origem] -= valor
        saldos[indice_destino] += valor
        transacoes.append({"de": indice_origem, "para": indice_destino, "valor": valor})
        print(f"[SUCESSO] Transferência de R${valor} concluída.")
    else:
        print("[ERRO] Saldo insuficiente.")

def mostrar_contas():
    print("\n--- STATUS ATUAL DO BANCO ---")
    print(f"{'Índice':<8} | {'Titular':<10} | {'Saldo':<10} | {'Tipo':<10}")
    print("-" * 45)
    for i in range(len(titulares)):
        print(f"{i:<8} | {titulares[i]:<10} | {saldos[i]:<10.2f} | {tipos[i]:<10}")

def manutencao_mensal(): #Linha acrecentada para a atividade
    for i in range(len(saldos)):
        if saldos[i] < 200:
            remover_conta(i)



if __name__ == "__main__":
    mostrar_contas()
    
    transferir(0, 1, 300)
    remover_conta(2) # Remove Charlie (Índice 2)
    
    
    mostrar_contas()
    print("\n[PERGUNTA] Quem é o titular do índice 2 agora? E quem era antes?")
    print("[DESAFIO] Implemente a 'manutencao_mensal()' sem quebrar o banco.")

print("\n--- HISTÓRICO DE TRANSAÇÕES ---")

for t in transacoes:
    origem = titulares[t["de"]]
    destino = titulares[t["para"]]

    print(origem, "->", destino, ":", t["valor"])