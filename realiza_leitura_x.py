import pandas as pd

def realiza_leitura_encaminha():
    arquivo1 = r'C:\Users\Gustavo\Downloads\Projeto_APS\data\Node_2.csv'
    arquivo2 = r'C:\Users\Gustavo\Downloads\Projeto_APS\data\Node_9.csv'
    arquivo3 = r'C:\Users\Gustavo\Downloads\Projeto_APS\data\Node_10.csv'


    dataframe1 = pd.read_csv(arquivo1, names=['Index', 'Value']) 
    dataframe2 = pd.read_csv(arquivo2, names=['Index', 'Value']) 
    dataframe3 = pd.read_csv(arquivo3, names=['Index', 'Value']) 

    dataframe1 = dataframe1.drop(columns=["Index"], axis=1)
    dataframe2 = dataframe2.drop(columns=["Index"], axis=1)
    dataframe3 = dataframe3.drop(columns=["Index"], axis=1)

    dataframeConcatenado = pd.concat([dataframe1, dataframe2, dataframe3], ignore_index=True, names=['Index', 'Value'])

    return dataframeConcatenado