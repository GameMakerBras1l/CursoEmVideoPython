inventario_senac = []

class equipamento_ti:
    def __init__(self, id_patrimonio, tipo, marca, valor_compra):
        self.id = id_patrimonio
        self.tipo = tipo
        self.marca = marca
        self.valor = valor_compra

        self.esta_ativo = True

    def __repr__(self):
        return f"id= {self.id}, tipo= {self.tipo}, marca= {self.marca} |{self.valor}|"


for i in range(0, 10):

    marca_ti = "Dell"

    if i % 2 == 0:
        marca_ti = "Apple"

    inventario_senac.append(equipamento_ti(i, "Notebook", marca_ti, 4500))


soma = 0

for item in inventario_senac:

    # soma do patrimônio ativo
    if item.esta_ativo:
        soma += item.valor

    # filtro por marca
    if item.marca == "Dell":
        print(item)


print("Total investido:", soma)