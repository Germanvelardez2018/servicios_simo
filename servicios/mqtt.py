import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from colorama import Fore, Back, Style, init
import servicios.db as db



print("mqtt client")

init() # init colorama
# Carga las variables de entorno desde el archivo .env
load_dotenv()
# Accede a las variables de entorno cargadas
MQTT_URL = os.getenv("MQTT_URL")
MQTT_PORT =1883
TOPICS_LIST = [
                "REQUEST",
                "RETCMD",
                "STATE",
                "CMD",
                "APP"
                ]




# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Conectado a Broker mqtt")




last_command = None
def _get_date(data):
    """Extrae la fecha de la nmea gps """
    elements = data.split(',')
    if elements == "":
        return None
    return  elements[0],elements[0][1:9]


def _get_params(frame):
    """Extrae parametros del comando"""
    params = frame.split(':')
    index =  int((params[0]))
    return params,index


def _insert_data(id,date,data):
    """ Inserta data en base de datos  """
    json = {}
    json["num"]=id
    json["data"]=data
    obj = db.find(date,**{"num":id})           
    if obj == None:
        print(Fore.BLUE + f"dato insertado:{json}")
        print(Style.RESET_ALL)
        db.insert_data(date,**json)



# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global last_command
    data = msg.payload.decode('utf-8')
    topic = msg.topic

    if topic == 'REQUEST':
        params,index = _get_params(data)
        print(f"Comando ejecutado:{params}")
        client.publish("APP",last_command,qos=2,retain=False)
        last_command = data
        client.publish("RETSHADOW",data,qos=2)
        return

    if topic == 'CMD':
        data = data[:-1]
        elements = data.split("|")
        for _data in elements:
            id,date = _get_date(_data)
            if date :
                _insert_data(id,date,_data)
            else:
                print(Fore.RED+"dato invalido, descartar")
                print(Style.RESET_ALL)


    if topic == 'RETCMD':
        print(f"Comando ejecutado, retorno {data}")
        last_command = None
        return

    if topic == 'STATE':
        print(f"Estado del dispositivos: \n{data}")
        if last_command is not None:
            print(f"ejecutando comando {last_command}")
            client.publish("APP",last_command,qos=2,retain=False)
            last_command = None
        return

    




_client = mqtt.Client(clean_session = True)
_client.on_connect = on_connect
_client.on_message = on_message
try:
    _client.connect(MQTT_URL,MQTT_PORT,60)
    for e in TOPICS_LIST:
        print(f"sub a {e}")
        _client.subscribe(e)
except Exception as e:
    print(f"Error:{e}")



def get_client():
    global _client
    return _client
    

