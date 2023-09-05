import servicios.db as db
import servicios.mqtt as mqtt
import time
import pprint






def get_date():
    #Obtengo la fecha de hoy y busco datos relacionados
        # Obtener la estructura de tiempo actual
    now = time.localtime()
    # Obtener el año, mes y día
    y = now.tm_year
    m = now.tm_mon if now.tm_mon > 9 else f"0{now.tm_mon}"
    d = now.tm_mday if now.tm_mday > 9 else f"0{now.tm_mday}"
    return f"{y}{m}{d}"


class App:
    def __init__(self,app_name="App",**config) -> None:
        self.name = app_name
        self.config = config
      

    def collections_list(self):
        collection_names = db.get_db().list_collection_names()
        return collection_names

    def find_data(self,date=None,**filters):
        if date is None:
            date = get_date()
        try:
            return db.find_list(date,**filters)
        except db.MongoException as e:
            print(f"Exception:{e}")
            return []
            
        
        


if __name__ == "__main__":

    TEST_MQTT = True


    if TEST_MQTT:
        print("test mqtt")
        client = mqtt.get_client()

        client.loop_forever()
        while True:
            pass

    else:

        print("test db")
        app = App("simo interface")
        filters = {}
        print("Lista de colecciones almacenadas:")
        clist = app.collections_list()
        for e in clist:
            print(f"\t{e}")
        date = input("Obtener datos de fecha yyyymmdd: ")
        data = app.find_data(date ,**filters)
        for element in data:
            pprint.pprint(element)
   