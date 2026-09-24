# Importamos a biblioteca argparse para recebermos a secret via parâmetro de linha de comando, sem versioná-la no código.
import argparse

# Importamos os módulos de configuração (config.py) e de instancia do servidor para executarmos a aplicação corretamente.
from src.config import app_config, app_active
from src.app import create_app, app, socketio

# Atribuímos o ambiente desejado para instanciarmos a aplicação.
config = app_config[app_active]

# Método responsável por iniciar o servidor, coleta em tempo real dos dados e iniciar o Machine Learning.
if __name__ == '__main__':

    # Lê a secret da aplicação a partir de um parâmetro de linha de comando (--secret), para que ela
    # nunca fique hardcoded no config.py nem versionada no repositório.
    parser = argparse.ArgumentParser(description='Sistema de Monitoramento e Gerenciamento de Sistemas Adutores de Água')
    parser.add_argument('--secret', dest='secret', default=None, help='Secret da aplicação. Não é obrigatória para o funcionamento local do dashboard.')
    args = parser.parse_args()

    # Atribui a secret recebida (se houver) à configuração antes da instância do servidor.
    config.SECRET = args.secret

    # Adiciona as configurações informadas acima, para correta instância do servidor.
    create_app(config)

    # Método que executa a aplicação.
    socketio.run(app, host=config.IP_HOST, port=config.PORT_HOST, debug=True)
