import servicios.db as db
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


    def get_data_by_date(self,date=None):
        if date is None:
            date = get_date() 
        print(f"find data from {date}")
        collection = db.get_collection(date)
        return collection
        

    def find_data(self,date=None,**filters):
        collection = self.get_data_by_date(date)
        print(f"filters:{filters}")
        return collection.find(filters)
     
        
        
     






if __name__ == "__main__":
    print("Iniciando el programa")
    print(f"date today is {get_date()}")
    app = App("simo interface")

    data = app.find_data("20230824")
    for element in data:
        pprint.pprint(element)
   