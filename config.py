import os

class Config():
    CSRF_ENABLE=True
    SECRET = '9T3P7X5K6H2J'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None