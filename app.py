from flask import Flask

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    config.APP = app

    @app.route('/')
    def index():
        return 'Hello Word'