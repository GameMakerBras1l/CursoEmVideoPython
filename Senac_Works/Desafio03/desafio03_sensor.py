class SensorAmbiente:
    def __init__(self, localizacao, temperatura, umidade):
        self.localizacao = localizacao
        self.temperatura = temperatura
        self.umidade = umidade

    def atualizar_leitura(self, nova_temp, nova_umidade):

        if nova_temp < -50.0 or nova_temp > 100.0:
            print("[ERRO] Temperatura inválida. Valor deve estar entre -50.0 e 100.0.")
            return

        if nova_umidade < 0 or nova_umidade > 100:
            print("[ERRO] Umidade inválida. Valor deve estar entre 0 e 100%.")
            return

        self.temperatura = nova_temp
        self.umidade = nova_umidade

    print("[OK] Leitura atualizada com sucesso.")

sensor = SensorAmbiente("Laboratório", 25.0, 40)

sensor.atualizar_leitura(30.5, 50)
sensor.atualizar_leitura(150, 30)
sensor.atualizar_leitura(20, 150)