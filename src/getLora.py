# Importação da biblioteca pandas para realizar a criação do DataFrame para o tratamento da interface.
import pandas as pd

# Importação da biblioteca de sistema operacional para localizarmos a pasta data/ na raiz do projeto.
import os

# Diretório da pasta data/ na raiz do projeto, um nível acima da pasta src/.
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

def realiza_leitura_encaminha():

    # Realiza a extração dos dados salvos em arquivos do LoRa de coleta em tempo real da velocidade da água vinda dos sensores.
    arquivo1 = os.path.join(DATA_DIR, 'Node_21.csv')
    arquivo2 = os.path.join(DATA_DIR, 'Node_91.csv')
    arquivo3 = os.path.join(DATA_DIR, 'Node_101.csv')

    # Realiza a conversão dos arquivos em formato CSV salvos pelo LoRa para um array do tipo DataFrame pandas.
    dataframe1 = pd.read_csv(arquivo1, names=['Index', 'Value']) 
    dataframe2 = pd.read_csv(arquivo2, names=['Index', 'Value']) 
    dataframe3 = pd.read_csv(arquivo3, names=['Index', 'Value']) 

    # Concatena as novas chegadas de dados em tempo real salvas em arquivos CSV diferentes do LoRa, para um único DataFrame contendo todas as informações/registros dos dados. 
    dataframeConcatenado = pd.concat([dataframe1, dataframe2, dataframe3], ignore_index=True)

    # Retorna para a interface os dados concatenados para exibição do usuário. 
    return dataframeConcatenado
