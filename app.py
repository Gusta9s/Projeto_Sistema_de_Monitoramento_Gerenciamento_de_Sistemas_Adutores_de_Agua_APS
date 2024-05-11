# Importando a biblioteca de funcionamento do servidor para nosso contexto de aplicação.
from flask import Flask, render_template

# Importando a biblioteca que permite a compilação dos dados em tempo real para a aplicação.
from flask_socketio import SocketIO

# Importando o módulo de extração dos dados vindos dos sensores de pressão e velocidade do adutor de água.
from getLora import realiza_leitura_encaminha

# Importando o módulo de aprendizado supervisionado dos dados vindos dos sensores.
from machineLearning import realiza_aprendizado_supervisionado

# Instância do servidor no contexto da aplicação.
app = Flask(__name__)

# Instância da biblioteca de coleta em tempo real dos dados vindos dos sensores.
socketio = SocketIO(app)

# Permite que o Template/Interface faça um autorecarregamento, a partir de novos dados vindos da extração dos sensores.
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Método de execução da aplicação no contexto do servidor.
def create_app(config):

    # Instância as variáveis de ambiente do config.py para dentro do nosso servidor.
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    config.APP = app

    # Após a requisição para o endpoint da URL (ex: /dashboard), damos os acessos e controlamos o que o cliente pode receber ou requisitar. (1 - A partir de qual origem (cliente URL) os dados podem ser requisitados para nossa aplicação. 2 - Cabeçalho de rede que o usuário pode receber da requisição. 3 - Os métodos de requisição HTTP que o cliente pode fazer para a aplicação no contexto de servidor.)
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    # Nosso endpoint inicial do contexto da aplicação, com o redirecionamento para demonstração do dashboard.
    @app.route('/')
    def index():
        return render_template('home.html')
    
    # Nosso endpoint principal da aplicação, contendo a coleta de dados em tempo real sendo direcionadas para o cliente, com todos os dados de Machine Learning de decisão e coleta bruta de dados vindos do LoRa já tratados.
    @app.route('/dashboard')
    def dashboard_view():
        dados = realiza_leitura_encaminha()
        array_dados = dados.values.tolist()
        machine_learning_dados = realiza_aprendizado_supervisionado()
        array_machine_learning = machine_learning_dados.tolist()
        return render_template('painel.html', dados=array_dados, array_machine_learning=array_machine_learning)
