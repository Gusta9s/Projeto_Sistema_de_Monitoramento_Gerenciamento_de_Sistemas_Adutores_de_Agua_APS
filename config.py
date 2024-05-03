import os

class config():
    CSRF_ENABLE=True
    SECRET = '9T3P7X5K6H2J'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None

class Dev(config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8080
    DASHBOARD = 'dashboard'
    URL_MAIN = 'http://%s/%s/%s' % (IP_HOST, PORT_HOST, DASHBOARD) # Este cara forma o endpoint inicial completo

class Prod(config):
    DEBUG = False
    TESTING = False
    IP_HOST = '192.0.5.3'
    PORT_HOST = 8080
    DASHBOARD = 'dashboard'
    URL_MAIN = 'http://%s/%s/%s' % (IP_HOST, PORT_HOST, DASHBOARD) # Este cara forma o endpoint inicial completo

app_config = {
    'dev' : Dev(),
    'prod' : Prod()
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'dev'