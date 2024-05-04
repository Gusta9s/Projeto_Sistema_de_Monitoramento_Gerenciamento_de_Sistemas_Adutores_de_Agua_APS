from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
from GetLora import realiza_leitura_encaminha

app = Flask(__name__)
socketio = SocketIO(app)

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
    
    @app.get('/dashboard/dados')
    def dados(): 
        page = request.args.get('page', default=1, type=int)
        numeros_por_pagina = 3
        start_indice = (page - 1) * numeros_por_pagina
        indice_final = start_indice + numeros_por_pagina
        dados = realiza_leitura_encaminha()
        array_dados = dados.values.tolist()
        arrayPaginado = array_dados[start_indice : indice_final]
        return jsonify({'dados' : arrayPaginado})
    
    @socketio.on('connect')
    def handle_connect():
        print('Client connected')

    @socketio.on('disconnect')
    def handle_disconnect():
        print('Client disconnected')

    @socketio.on('lora_logs')
    def lora_logs(data):
        lora_logs = data['lora_logs']
        socketio.emit('lora_logs', {'lora_logs': lora_logs})

    @socketio.on('update_ml_logs')
    def update_ml_logs(data):
        emit('update_ml_logs', data, broadcast=True)

    @socketio.on('update_alert')
    def update_alert(alert):
        emit('update_alert', alert, broadcast=True)