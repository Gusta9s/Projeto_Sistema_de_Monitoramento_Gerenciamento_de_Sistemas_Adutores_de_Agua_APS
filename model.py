class Dados:
    
    def __init__(self, peso, velocidade, extensao):
        self.peso = peso
        self.velocidade = velocidade
        self.extensao = extensao
        self.array_peso = []
        self.array_velocidade = []
        self.array_extensao = []
        self.adiciona_peso(self.peso)
        self.adiciona_velocidade(self.velocidade)
        self.adiciona_extensao(self.extensao)

    def adiciona_peso(self, valor):
        self.array_peso.append(valor)

    def adiciona_velocidade(self, valor):
        self.array_velocidade.append(valor)

    def adiciona_extensao(self, valor):
        self.array_extensao.append(valor)

    
