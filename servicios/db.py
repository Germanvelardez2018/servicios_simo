""""
 Servicios de base de datos


"""
import pymongo
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()








# Accede a las variables de entorno cargadas
DB_URL = os.getenv("MONGO_URL")
DB_DEFAULT_NAME = os.getenv("DB_DEFAULT_NAME")




def get_client(url=DB_URL):
    """ Devuelve el cliente Mongo"""
    return pymongo.MongoClient(url)


def get_db(db_name=DB_DEFAULT_NAME,db_url = DB_URL):
    """Devuelve la base de datos"""
    client = get_client(db_url)
    return  client[db_name]
   
 
def get_collection(collection_name,db_name=DB_DEFAULT_NAME,db_url=DB_URL):
    """Devuelve la coleccion de datos"""
    db = get_db(db_name)
    return  db[collection_name]

