from flask import Flask, render_template
from flask_socketio import SocketIO, emit

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
        return render_template('painel.html')
    
    @socketio.on('update_header')
    def update_header(data):
        emit('update_header', data, broadcast=True)

    @socketio.on('update_lora_logs')
    def update_lora_logs(data):
        emit('update_lora_logs', data, broadcast=True)

    @socketio.on('update_ml_logs')
    def update_ml_logs(data):
        emit('update_ml_logs', data, broadcast=True)

    @socketio.on('update_alert')
    def update_alert(alert):
        emit('update_alert', alert, broadcast=True)