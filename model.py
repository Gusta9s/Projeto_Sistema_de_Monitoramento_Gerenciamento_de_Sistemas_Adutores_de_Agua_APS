# Importamos os módulos de extração dos dados de coleta em tempo real do LoRa para nossas features de aprendizado supervisionado.
from realiza_leitura_x import realiza_leitura_encaminha
from realiza_leitura_y import realiza_leitura_y

class Dados:
    
    # Definimos nossos atributos essenciais e arrays essenciais para o correto funcionamento do aprendizado supervisionado.
    def __init__(self, velocidade, excesso):
        self.velocidade = velocidade
        self.excesso = excesso
        self.array_velocidade = []
        self.array_excesso = []

    # Definimos nosso método para inclusão nos arrays de velocidade e pressão os dados de coleta em tempo real do LoRa.
    def adiciona_velocidade(self):
        self.array_velocidade.append(self.velocidade)

    def adiciona_excesso(self):
        self.array_excesso.append(self.excesso)

# Instância da nossa classe, realizando os processos de coleta e inclusão nos arrays de Machine Learning para aprendizado supervisionado.
def realiza_criacao_objeto():
    dataframe_x = realiza_leitura_encaminha()
    dataframe_y = realiza_leitura_y()

    # Inclusão dos dados obtidos através de leitura para nosso array temporário de dados.
    list_x = dataframe_x['Value'].values.tolist()
    list_y = dataframe_y['Value'].values.tolist()

    # A instância da classe para aprendizado supervisionado.
    dados_x = Dados(velocidade=list_x, excesso=list_y)

    # Inclusão dos registros contidos dentro do array temporário para nossos arrays da classe formando nossas features.
    dados_x.adiciona_velocidade()
    dados_x.adiciona_excesso()

    # Encaminhamento para nosso arquivo machineLearning.py do objeto contendo nossas features para tratamento e tomada de decisões em tempo real.
    return dados_x
