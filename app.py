from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
from getLora import realiza_leitura_encaminha

app = Flask(__name__)
socketio = SocketIO(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True


def create_app(config):
    app.config.from_object(config)
    app.config.from_pyfile('config.py')
    config.APP = app

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def index():
        return render_template('home.html')
    
    @app.route('/dashboard')
    def dashboard_view():
        dados = realiza_leitura_encaminha()
        array_dados = dados.values.tolist()
        return render_template('painel.html', dados=array_dados)