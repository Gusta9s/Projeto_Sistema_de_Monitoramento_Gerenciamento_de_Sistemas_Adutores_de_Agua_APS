import time
import socketio
from config import app_active, app_config
                
def connection_sio ():
    # standard Python
    sio = socketio.SimpleClient()

    config = app_config[app_active]

    sio.connect(config.URL_MAIN) #transports=['websocket']

    print('my sid is', sio.sid)

    print('my transport is', sio.transport) 

    arquivos_csv = [
        r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_2.csv',
        r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_9.csv',
        r'C:\Users\Gustavo\Downloads\dadoscsvnet\Net1_CMH\Scenario-1\Demands\Node_10.csv'
    ]
    
    for arquivo in arquivos_csv:
        with open(arquivo, 'r') as file:
            for linha in file:
                dados = linha.strip()
                sio.emit('lora_logs', dados)
                time.sleep(2)
    
    sio.disconnect()