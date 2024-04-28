from flask import Flask
from admin.Admin import start_views
from flask_bootstrap import Bootstrap

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    app.config['FLASK_ADMIN_SWATCH'] = 'paper'
    start_views(app)
    Bootstrap(app)
    config.APP = app

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def index():
        return 'Hello Word'