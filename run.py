from config import app_config, app_active
from app import create_app, app, socketio
from getLora import connection_sio

config = app_config[app_active]

if __name__ == '__main__':
    create_app(config)
    socketio.run(app, host=config.IP_HOST, port=config.PORT_HOST, debug=True)

