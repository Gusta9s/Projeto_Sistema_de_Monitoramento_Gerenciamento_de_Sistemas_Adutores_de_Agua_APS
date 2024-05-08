import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from model import realiza_criacao_objeto

def apply_transformacao_x(valor):
    if valor == 0:
        return 1
    else:
        return 0

def apply_transformacao_y(valor):
    if valor == 45.72:
        return 1
    else:
        return 0
    

dados_x = realiza_criacao_objeto()

SEED = 14

np.random.seed(SEED)

dt1 = pd.DataFrame(dados_x.array_velocidade[0])
dt2 = pd.DataFrame(dados_x.array_excesso[0])

dt2.columns = ['1']

dt_combinado = pd.concat([dt1, dt2], axis=1)

dt_combinado = dt_combinado.rename(columns={0: 'Velocidade S.Atual', '1': 'Pressao S.Anterior'})

#array1 = dt_combinado['Velocidade S.Atual'].values

#parte0 = np.array_split(array1, 2)

percent_701 = int(len(dt_combinado['Velocidade S.Atual']) * 0.7)
percent_702 = int(len(dt_combinado['Pressao S.Anterior']) * 0.7)

dataframe_70_percent1 = dt_combinado['Velocidade S.Atual'].sample(n=percent_701)
dataframe_70_percent2 = dt_combinado['Pressao S.Anterior'].sample(n=percent_702)

dataframe_30_percent1 = dt_combinado['Velocidade S.Atual'].drop(dataframe_70_percent1.index)
dataframe_30_percent2 = dt_combinado['Pressao S.Anterior'].drop(dataframe_70_percent2.index)

#parte1 = parte0[0]

#parte2 = parte0[1]

#array2 = dt_combinado['Pressao S.Anterior'].values

#parte00 = np.array_split(array2, 2)

#parte11 = parte00[0]

#parte22 = parte00[1]

#treino_x = pd.DataFrame(parte1)

#test_x = pd.DataFrame(parte2)

#treino_y = pd.DataFrame(parte11)

#test_y = pd.DataFrame(parte22)

#test_x.columns = ['1']
#treino_y.columns = ['2']
#test_y.columns = ['3']

#dt_combinado = pd.concat([treino_x, test_x, treino_y, test_y], axis=1)

#dt_combinado = dt_combinado.rename(columns={0: 'Velocidade S.Atual Treino', '1': 'Velocidade S.Atual Test', '2': 'Pressao S.Anterior Treino', '3': 'Pressao S.Anterior Test'})

#features = dt_combinado[['Velocidade S.Atual Treino', 'Velocidade S.Atual Test']]

#labels = dt_combinado[['Pressao S.Anterior Treino', 'Pressao S.Anterior Test']]

#x_train, x_test, y_train, y_test = train_test_split(dataframe_70_percent, labels.iloc[:,1], test_size=0.3, stratify=labels.iloc[:,1])

dataframe_70_percent1 = pd.DataFrame({'Velocidade S.Atual Treino' : dataframe_70_percent1})
dataframe_70_percent2 = pd.DataFrame({'Pressao S.Anterior Treino': dataframe_70_percent2})
dataframe_30_percent1 = pd.DataFrame({'Velocidade S.Atual Test': dataframe_30_percent1})
dataframe_30_percent2 = pd.DataFrame({'Pressao S.Anterior Test': dataframe_30_percent2})

dataframe_70_percent1 = pd.concat([dataframe_70_percent1, dataframe_30_percent1], axis=1)

dataframe_70_percent1['Velocidade S.Atual Treino'] = dataframe_70_percent1['Velocidade S.Atual Treino'].apply(apply_transformacao_x)
dataframe_70_percent1['Velocidade S.Atual Test'] = dataframe_70_percent1['Velocidade S.Atual Test'].apply(apply_transformacao_x)

dataframe_70_percent1 = dataframe_70_percent1.reset_index(drop=True)

dataframe_30_percent10 = pd.concat([dataframe_70_percent2, dataframe_30_percent2], ignore_index=True)

dataframe_30_percent10['Pressao S.Anterior Treino'] = dataframe_30_percent10['Pressao S.Anterior Treino'].apply(apply_transformacao_y)

dataframe_30_percent10 = dataframe_30_percent10.drop(columns=['Pressao S.Anterior Test'])

dataframe_30_percent10 = dataframe_30_percent10.rename(columns={'Pressao S.Anterior Treino' : 'Pressao S.Anterior'})

dataframe_30_percent10 = dataframe_30_percent10.reset_index(drop=True)

#print(dataframe_30_percent1.head())

modelo = LinearSVC(dual=True)

scaller = StandardScaler()

x_train, x_test, y_train, y_test = train_test_split(dataframe_70_percent1, dataframe_30_percent10, test_size=0.4, stratify=dataframe_30_percent10)

x_train_scaled = scaller.fit_transform(x_train)
x_test_scaled = scaller.transform(x_test)

y_train_reshaped = y_train.values.ravel()

modelo.fit(x_train_scaled, y_train_reshaped)

previsoes = modelo.predict(x_test_scaled)

acuracia = accuracy_score(y_test, previsoes) * 100

#print(f'A acuracia do teste e: {acuracia:.2f}')