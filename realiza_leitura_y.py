import pandas as pd

def realiza_leitura_y():

    arquivo4 = r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Pressures\Node_2.csv'
    arquivo5 = r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Pressures\Node_9.csv'
    arquivo6 = r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Pressures\Node_10.csv'

    dataframe1 = pd.read_csv(arquivo4, names=['Index', 'Value'])
    dataframe2 = pd.read_csv(arquivo5, names=['Index', 'Value'])
    dataframe3 = pd.read_csv(arquivo6, names=['Index', 'Value'])

    dataframe1 = dataframe1.drop(columns=["Index"], axis=1)
    dataframe2 = dataframe2.drop(columns=['Index'], axis=1)
    dataframe3 = dataframe3.drop(columns=['Index'], axis=1)

    dataframe_concatenado = pd.concat([dataframe1, dataframe2, dataframe3], ignore_index=True, names=['Index', 'Value'])
    return dataframe_concatenado
