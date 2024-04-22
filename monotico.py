import pandas as pd
import time

arquivos_csv = [
    r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_2.csv',
    r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_9.csv',
    r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_10.csv'
]

arquivo1 = r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_2.csv'
arquivo2 = r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_9.csv'
arquivo3 = r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_10.csv'
arquivo4 = r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Leaks\Leak_13_demand.csv'

# Loop para simular a leitura em tempo real
for arquivo in arquivos_csv:
    # Abrindo o arquivo em modo de leitura
    with open(arquivo, 'r') as file:
        # Lendo cada linha do arquivo
        for linha in file:
            # Exibindo a linha lida no console
            print(linha.strip())  # strip() remove espaços em branco extras
            # Espera de 1 segundo entre cada linha (simulando leitura em tempo real)
            time.sleep(2)


dataframe1 = pd.read_csv(arquivo1)
dataframe2 = pd.read_csv(arquivo2)
dataframe3 = pd.read_csv(arquivo3)
dataframe4 = pd.read_csv(arquivo4)

dataframeConcatenado = pd.concat([dataframe1, dataframe2, dataframe3], ignore_index=True)

print(f'/n', dataframeConcatenado[:1000])