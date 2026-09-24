# Importamos a biblioteca de sistema operacional para nosso projeto, para que possamos realizar a leitura dos caminhos de uma forma mais simplificada.
import os

# Instanciamos nossas variáveis de ambiente essenciais para bom funcionamento no ambiente local, quanto de produção.
class Config():
    CSRF_ENABLE = True
    # Diretório raiz do projeto, um nível acima da pasta src/ onde este arquivo está localizado.
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None
    # Chave secreta da aplicação. Não é definida aqui: run.py a recebe via parâmetro de linha de
    # comando (--secret) e a atribui a esta classe antes de create_app() ser chamado, para que o
    # valor nunca fique hardcoded ou versionado no código-fonte.
    SECRET = None

# Instância das variáveis de ambiente do ambiente local/desenvolvimento.
class Dev(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    DASHBOARD = 'dashboard'
    URL_MAIN = f'http://{IP_HOST}/{PORT_HOST}'

# Instância das variáveis de ambiente do ambiente de produção.
class Prod(Config):
    DEBUG = False
    TESTING = False
    IP_HOST = '127.0.0.1'
    PORT_HOST = 8080
    DASHBOARD = 'dashboard'
    URL_MAIN = f'http://{IP_HOST}/{PORT_HOST}'

# A partir da carga no terminal, inclua e acione o ambiente escolhido.
app_config = {
    'dev': Dev(),
    'prod': Prod()
}

# No terminal é incluído o ambiente desejado para executar a aplicação e se nenhum valor for incluído o ambiente é automaticamente incluído como local.
app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'dev'
