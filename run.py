# Importamos os módulos de configuração (config.py) e de instancia do servidor para executarmos a aplicação corretamente.
from config import app_config, app_active
from app import create_app, app, socketio

# Atribuímos o ambiente desejado para instanciarmos a aplicação.
config = app_config[app_active]

# Método responsável por iniciar o servidor, coleta em tempo real dos dados e iniciar o Machine Learning.
if __name__ == '__main__':

    # Adiciona as configurações informadas acima, para correta instância do servidor.
    create_app(config)

    # Método que executa a aplicação.
    socketio.run(app, host=config.IP_HOST, port=config.PORT_HOST, debug=True)
