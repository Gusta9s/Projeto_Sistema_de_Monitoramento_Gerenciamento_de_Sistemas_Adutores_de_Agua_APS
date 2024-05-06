from realiza_leitura_x import realiza_leitura_encaminha
from realiza_leitura_y import realiza_leitura_y

class Dados:
    
    def __init__(self, velocidade, excesso):
        self.velocidade = velocidade
        self.excesso = excesso
        self.array_velocidade = []
        self.array_excesso = []

    def adiciona_velocidade(self):
        self.array_velocidade.append(self.velocidade)

    def adiciona_excesso(self):
        self.array_excesso.append(self.excesso)

def realiza_criacao_objeto():
    dataframe_x = realiza_leitura_encaminha()
    dataframe_y = realiza_leitura_y()

    list_x = dataframe_x['Value'].values.tolist()
    list_y = dataframe_y['Value'].values.tolist()

    dados_x = Dados(velocidade=list_x, excesso=list_y)
    dados_x.adiciona_velocidade()
    dados_x.adiciona_excesso()

    return dados_x
    
