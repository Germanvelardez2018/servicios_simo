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
COLLECTION_DEFUALT_NAME = os.getenv("COLLECTION_DEFUALT_NAME")




client =pymongo.MongoClient(DB_URL) 



def get_db(db_name=DB_DEFAULT_NAME):
    return client[db_name]
 
def get_collection(collection_name=COLLECTION_DEFUALT_NAME,db_name=DB_DEFAULT_NAME):
    return (client[db_name])[collection_name] 

