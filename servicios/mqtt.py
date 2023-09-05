import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv


# Carga las variables de entorno desde el archivo .env
load_dotenv()
# Accede a las variables de entorno cargadas
DB_URL = os.getenv("BROKER_MQTT")
DB_DEFAULT_NAME = os.getenv("DB_DEFAULT_NAME")