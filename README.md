# Sistema de Monitoramento e Gerenciamento de Sistemas Adutores de Água

Aplicação web em **Python (Flask + Flask-SocketIO)** que monitora, em tempo real, a pressão e a velocidade da água em um sistema adutor a partir de sensores LoRa, aplica um modelo de **aprendizado supervisionado (SVC)** sobre esses dados e exibe em um dashboard se há indício de vazamento no sistema.

Este projeto é uma **APS (Atividade Prática Supervisionada)** da UNIP, independente do TCC de Gestão de Resíduos Sólidos Urbanos (SWM) e dos demais projetos de reconhecimento facial — é um exercício acadêmico de monitoramento de infraestrutura hídrica com sensoriamento remoto e machine learning.

## O problema

Vazamentos em sistemas adutores de água costumam ser identificados tardiamente, quando já causaram perda significativa de água ou dano à infraestrutura, porque a inspeção é normalmente manual e pontual. O desafio técnico do projeto foi simular um sistema de monitoramento contínuo: coletar em tempo real os dados de pressão e velocidade da água vindos de sensores (via rede LoRa), processá-los e usar um modelo de aprendizado de máquina para inferir automaticamente se o padrão observado indica um possível vazamento — em vez de depender de um limiar fixo ou de inspeção manual.

## A solução

O backend foi construído em **Python com Flask**, escolha natural pela simplicidade de expor um dashboard web e integrar bibliotecas de dados científicos (pandas, scikit-learn) no mesmo processo que atende as requisições HTTP. O **Flask-SocketIO** foi adicionado para permitir a atualização do dashboard em tempo real, à medida que novos dados dos sensores chegam. Os dados de pressão e velocidade, coletados pelos sensores via LoRa e salvos em arquivos CSV, são carregados com pandas e transformados em features binárias segundo regras de negócio simples (ex.: velocidade zero, pressão acima de um valor de referência). Sobre essas features, um classificador **SVC (Support Vector Classifier)** do scikit-learn foi treinado para prever, a cada nova leitura, se aquele padrão de velocidade/pressão é compatível com um vazamento — encapsulando a lógica de decisão em um modelo estatístico em vez de regras fixas espalhadas pelo código.

## O resultado

O pipeline funciona de ponta a ponta: os dados brutos dos três nós de sensores (LoRa) são lidos e concatenados, transformados em features de velocidade e pressão, e classificados pelo modelo SVC treinado a cada execução, que reporta a acurácia do teste e a decisão ("Sim"/"Não" há vazamento) para cada leitura. O dashboard web (/dashboard) exibe três áreas em tempo real: um alerta visual em caso de vazamento, o histórico das decisões tomadas pelo modelo de machine learning e o log bruto dos dados recebidos dos sensores — permitindo acompanhar tanto a decisão final quanto os dados que a originaram.

## Como o sistema funciona

1. **Coleta**: os sensores de pressão e velocidade instalados no adutor enviam leituras via rede LoRa, salvas em arquivos CSV por nó.
2. **Extração**: a aplicação lê e concatena os arquivos CSV dos diferentes nós em um único conjunto de dados.
3. **Preparo das features**: os valores de velocidade e pressão são convertidos em variáveis binárias com base em regras de negócio do domínio (adutores de água).
4. **Classificação**: um modelo SVC treinado a cada execução prevê se o padrão de leitura atual indica vazamento.
5. **Exibição**: o servidor Flask, com Flask-SocketIO, envia os dados brutos e a decisão do modelo para o dashboard, atualizado em tempo real.

## Como executar

```bash
pip install -r requirements.txt
python run.py
```

Por padrão, a aplicação sobe em modo de desenvolvimento (FLASK_ENV não definido) e o dashboard fica disponível na rota /dashboard.

### Secret da aplicação

A aplicação possui uma configuração `SECRET` (`src/config.py`) que **não é hardcoded nem versionada** no repositório. Ela deve ser informada por parâmetro de linha de comando ao iniciar o servidor:

```bash
python run.py --secret "<valor-da-secret>"
```

Se `--secret` não for informado, a aplicação sobe normalmente com `SECRET = None` — o parâmetro não é obrigatório para o funcionamento local do dashboard, mas deve ser definido com um valor próprio (não compartilhado publicamente) em qualquer ambiente exposto além do localhost.

## Estrutura do projeto

```
.
├── run.py                    # Ponto de entrada: carrega a configuração e inicia o servidor
├── src/                       # Código-fonte da aplicação
│   ├── app.py                 # Aplicação Flask + Flask-SocketIO e definição das rotas
│   ├── config.py               # Configurações de ambiente (dev/prod)
│   ├── getLora.py               # Leitura e concatenação dos dados brutos dos sensores (LoRa)
│   ├── realiza_leitura_x.py     # Leitura da feature de velocidade da água
│   ├── realiza_leitura_y.py     # Leitura da feature de pressão da água
│   ├── model.py                 # Classe de domínio que organiza os dados para o aprendizado supervisionado
│   └── machineLearning.py       # Treinamento do modelo SVC e tomada de decisão (vazamento ou não)
├── data/                     # Arquivos CSV com as leituras dos sensores
├── models/                   # Modelos de aprendizado supervisionado persistidos (quando aplicável)
├── tests/                    # Testes automatizados do projeto
├── notebooks/                # Notebooks de exploração e análise dos dados
├── docs/                     # Documentação complementar do projeto
├── templates/                # Páginas HTML (página inicial e dashboard em tempo real)
└── static/img/                # Imagens usadas na interface (ex.: ícone de alerta)
```

## Tecnologias principais

- Python / Flask / Flask-SocketIO
- pandas / NumPy
- scikit-learn (SVC, StandardScaler, train_test_split)
- HTML / CSS / jQuery (dashboard)
- Sensores LoRa

## Autor

Gustavo de Almeida Pacheco — desenvolvido como Atividade Prática Supervisionada (APS) na UNIP.
