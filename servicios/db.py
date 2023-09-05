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


class MongoException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)



def get_client(url):
    """ Devuelve el cliente Mongo"""
    print(f"client mongo url {url}")
    return pymongo.MongoClient(url)


def get_db(db_name=DB_DEFAULT_NAME,db_url = DB_URL):
    """Devuelve la base de datos"""
    client = get_client(db_url)
    return client[db_name]
   
 
def get_collection(collection_name,db_name=DB_DEFAULT_NAME,db_url=DB_URL):
    """Devuelve la coleccion de datos"""
    db = get_db(db_name)
    return  db[collection_name]



def find_list(collection_name,**filters):
    try:
        print("find list")
        collection = get_collection(collection_name)
        print(f"collection :{collection} ")
        print(f"filters:{filters}")
        result = collection.find(filters)
        print(f"result={result}")
        for i in result:
            print(i)
        return result
    except Exception as e:
        raise   MongoException(f"Error al listar collection {collection_name}")
    


def find(collection_name,**filters):
    try:
        collection = get_collection(collection_name)
        return collection.find_one(filters)
    except Exception as e:
        raise MongoException(f"Error al insertar dato en collection {collection_name}")





def insert_data(collection_name,**data):
    try:
        collection = get_collection(collection_name)
        collection.insert_one(data)
    except Exception as e:
        raise MongoException (f"Error al insertar dato en collection {collection_name}")
    
    