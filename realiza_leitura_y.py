# Importação da biblioteca pandas para realizar a criação do DataFrame para o tratamento do Machine Learning.
import pandas as pd

def realiza_leitura_y():

    # Realiza a extração dos dados salvos em arquivos do LoRa de coleta em tempo real de pressão de água vinda dos sensores.
    arquivo4 = r'C:\Users\Gustavo\Downloads\Projeto_APS\data\Node_2.csv'
    arquivo5 = r'C:\Users\Gustavo\Downloads\Projeto_APS\data\Node_9.csv'
    arquivo6 = r'C:\Users\Gustavo\Downloads\Projeto_APS\data\Node_10.csv'

    # Realiza a conversão dos arquivos em formato CSV salvos pelo LoRa para um array do tipo DataFrame pandas.
    dataframe1 = pd.read_csv(arquivo4, names=['Index', 'Value'])
    dataframe2 = pd.read_csv(arquivo5, names=['Index', 'Value'])
    dataframe3 = pd.read_csv(arquivo6, names=['Index', 'Value'])

    # Remove a coluna "Index" dos DataFrames.
    dataframe1 = dataframe1.drop(columns=["Index"], axis=1)
    dataframe2 = dataframe2.drop(columns=["Index"], axis=1)
    dataframe3 = dataframe3.drop(columns=["Index"], axis=1)

    # Concatena as novas chegadas de dados em tempo real salvas em arquivos CSV diferentes do LoRa, para um único DataFrame contendo todas as informações/registros dos dados.
    dataframe_concatenado = pd.concat([dataframe1, dataframe2, dataframe3], ignore_index=True)

    # Retorna para o Machine Learning os dados de sensores de pressão de água em tempo real, para tomada de decisão.
    return dataframe_concatenado
