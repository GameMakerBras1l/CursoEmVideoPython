class EquipamentoTI:
    def __init__(self, id_patrimonio, tipo, marca, valor_compra):
        self.id_patrimonio = id_patrimonio
        self.tipo = tipo
        self.marca = marca
        self.valor_compra = valor_compra
        self.esta_ativo = True

    def __str__(self):
        if self.esta_ativo:
            status = "ATIVO"
        else:
            status = "INATIVO"

        return f"[{status}] {self.tipo} {self.marca} (Patrimônio: {self.id_patrimonio})"


equip1 = EquipamentoTI(12345, "Notebook", "Dell", 4500)

print(equip1)