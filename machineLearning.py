import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from model import realiza_criacao_objeto

dados_x = realiza_criacao_objeto()

dt1 = pd.DataFrame(dados_x.array_velocidade[0])
dt2 = pd.DataFrame(dados_x.array_excesso[0])

dt2.columns = ['1']

dt_combinado = pd.concat([dt1, dt2], axis=1)

dt_combinado = dt_combinado.rename(columns={0: 'Velocidade S.Atual', '1': 'Pressao S.Anterior'})

array1 = dt_combinado['Velocidade S.Atual'].values

parte0 = np.array_split(array1, 2)

parte1 = parte0[0]

parte2 = parte0[1]

array2 = dt_combinado['Pressao S.Anterior'].values

parte00 = np.array_split(array2, 2)

parte11 = parte00[0]

parte22 = parte00[1]

treino_x = pd.DataFrame(parte1)

test_x = pd.DataFrame(parte2)

treino_y = pd.DataFrame(parte11)

test_y = pd.DataFrame(parte22)

test_x.columns = ['1']
treino_y.columns = ['2']
test_y.columns = ['3']

dt_combinado = pd.concat([treino_x, test_x, treino_y, test_y], axis=1)

dt_combinado = dt_combinado.rename(columns={0: 'Velocidade S.Atual Treino', '1': 'Velocidade S.Atual Test', '2': 'Pressao S.Anterior Treino', '3': 'Pressao S.Anterior Test'})

features = dt_combinado[['Velocidade S.Atual Treino', 'Velocidade S.Atual Test']]

labels = dt_combinado[['Pressao S.Anterior Treino', 'Pressao S.Anterior Test']]

SEED = 10

np.random.seed(SEED)

x_train, x_test, y_train, y_test = train_test_split(features, labels.iloc[:,1], test_size=0.3, stratify=labels.iloc[:,1])

modelo = DecisionTreeClassifier(max_depth=3)

modelo.fit(x_train, y_train)

previsoes = modelo.predict(x_test)

acuracia = accuracy_score(y_test, previsoes) * 100

print(f'A acuracia do teste e: {acuracia:.2f}')

