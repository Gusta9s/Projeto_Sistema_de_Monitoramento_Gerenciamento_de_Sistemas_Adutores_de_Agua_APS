# Importação do módulo pandas para criação dos dataframes neste contexto de projeto e realização de treino e teste do aprendizado supervisionado.
import pandas as pd

# Importação da biblioteca NumPy para incrementação de SEED (Semente) de geração do train_test_split e conversão de previsões para este tipo de array para retorno à interface.
import numpy as np

# Importação deste módulo da biblioteca Sklearn para gerarmos o modelo de aprendizado supervisionado baseado no modelo "Support Vector Classifier" ou Suporte para vetores de classificação, para objetos.
from sklearn.svm import SVC

# Importação deste módulo da biblioteca Sklearn para redimensionarmos as escalas das nossas features convertidas em objetos do tipo dataframe pandas.
from sklearn.preprocessing import StandardScaler

# Importação deste módulo da biblioteca Sklearn para realizarmos a divisão entre treino e teste para o aprendizado supervisionado do modelo "SVC()"
from sklearn.model_selection import train_test_split

# Importação deste módulo da biblioteca Sklearn para calcularmos a acurácia de acerto dos testes do aprendizado supervisionado do modelo "SVC()"
from sklearn.metrics import accuracy_score

# Importamos o modelo do arquivo model.py para realizarmos a instância do Objeto "__init__" para nosso aprendizado supervisionado.
from model import realiza_criacao_objeto


# Este método realiza a conversão de dados dinâmicos para dados estáticos, com base na regra de negócio dos adutores de água. Neste caso para nossa feature de velocidade por segundo da água no adutor.
def apply_transformacao_x(valor):
    if valor == 0:
        return 1
    else:
        return 0


# Este método realiza a conversão de dados dinâmicos para dados estáticos, com base na regra de negócio dos adutores de água. Neste caso para nossa feature de pressão por segundo da água no adutor.
def apply_transformacao_y(valor):
    if valor == 45.72:
        return 1
    else:
        return 0
    

# Este método realiza, com base na regra de negócio, a conversão de dados para nossa label, com base na velocidade e pressão da água no adutor por segundo, o retorno com possível vazamento "especulado".
def apply_etiqueta(row):
    if row['Velocidade S.Atual'] == 0 and row['Pressao S.Anterior'] == 0:
        return 0
    elif row['Velocidade S.Atual'] == 1 and row['Pressao S.Anterior'] == 1:
        return 1
    else:
        return 0
    
def realiza_aprendizado_supervisionado():

    # Extrai os dados do modelo.
    dados_x = realiza_criacao_objeto()

    # Gera uma semente de criação padronizada, para cada chegada nova de dados de pressão e velocidade no adutor.
    SEED = 0

    np.random.seed(SEED)

    # Extrai os arrays de velocidade e pressão do objeto. 
    dt1 = pd.DataFrame(dados_x.array_velocidade[0])
    dt2 = pd.DataFrame(dados_x.array_excesso[0])

    # Renomeia a coluna do array de pressão.
    dt2.columns = ['1']

    # Gera um DataFrame contendo os dois arrays em um único dataframe, formando a concretização da nossa feature.
    dt_combinado = pd.concat([dt1, dt2], axis=1)

    # Renomeia o DataFrame, para que tenha nomes convenientes para cada propósito no DataFrame.
    dt_combinado = dt_combinado.rename(columns={0: 'Velocidade S.Atual', '1': 'Pressao S.Anterior'})

    # Aplica a conversão de dados dinâmicos para estáticos nas nossas features e cria a nossa label com base na velocidade e pressão atuais.
    dt_combinado['Velocidade S.Atual'] = dt_combinado['Velocidade S.Atual'].apply(apply_transformacao_x)
    dt_combinado['Pressao S.Anterior'] = dt_combinado['Pressao S.Anterior'].apply(apply_transformacao_y)
    dt_combinado['Etiqueta'] = dt_combinado.apply(apply_etiqueta, axis=1)

    # Remove a sujeira de índice do próprio DataFrame pandas.
    dt_combinado = dt_combinado.reset_index(drop=True)

    # Criamos um DataFrame features para separação de features e labels, que no contexto anterior estavam juntas e precisam ficar separadas para o train_test_split(). 
    features = dt_combinado[['Velocidade S.Atual', 'Pressao S.Anterior']]
    labels = dt_combinado[['Etiqueta']]

    # Instância do Modelo de aprendizado supervisionado da aplicação.
    modelo = SVC()

    # Instância do Redimensionador de Escala da aplicação. 
    scaller = StandardScaler()

    # Aplicação da separação de dados para treino e de dados para teste, para correto funcionamento do modelo de aprendizado supervisionado.
    x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.9999, stratify=labels)

    # Redimensionamento de Escala para nossas features para maior nível de acertos do aprendizado supervisionado, por conta da diminuição de escala.
    x_train_scaled = scaller.fit_transform(x_train)
    x_test_scaled = scaller.transform(x_test)

    # Remoção de sujeira, removendo a espaços vazios de uma coluna, transformando esta em uma coluna unidirecional.
    y_train_reshaped = y_train.values.ravel()

    # Treinamento do modelo SVC() com o redimensionamento de escala aplicado para o x.
    modelo.fit(x_train_scaled, y_train_reshaped)

    # Os nossos dados em tempo real sendo calculados e feita tomada de decisão, informando se existe ou não vazamento de água no sistema de adutor. 
    previsoes = modelo.predict(x_test_scaled)

    # Verificamos se os resultados do teste são 100% corretos ou não.
    acuracia = accuracy_score(y_test, previsoes) * 100

    # Renomeamos nossos dados estáticos para dados dinâmicos para uma melhor visualização na interface.
    previsoes = np.where(previsoes == 0, 'Não', 'Sim')
    
    # Encaminhamos para interface a tomada de decisões em tempo real dos dados de velocidade e pressão da água, se existe vazamento ou não.
    return previsoes
