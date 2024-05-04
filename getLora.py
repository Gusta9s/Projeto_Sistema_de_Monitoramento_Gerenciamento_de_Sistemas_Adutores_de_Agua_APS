import pandas as pd

def realiza_leitura_encaminha ():
    
    arquivo1 = r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_2.csv'
    arquivo2 = r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_9.csv'
    arquivo3 = r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_10.csv'


    dataframe1 = pd.read_csv(arquivo1, names=['Index', 'Value']) 
    dataframe2 = pd.read_csv(arquivo2, names=['Index', 'Value']) 
    dataframe3 = pd.read_csv(arquivo3, names=['Index', 'Value']) 

    dataframeConcatenado = pd.concat([dataframe1, dataframe2, dataframe3], ignore_index=True, names=['Index', 'Value']) # neste arquivo gere uma paginacao de 10 em 10 paginas
    
    paginas = []
    for i in range(0, len(dataframeConcatenado), 10):
        pagina = dataframeConcatenado.iloc[i:i+10]
        paginas.append(pagina)

    print(paginas)
    return paginas
     