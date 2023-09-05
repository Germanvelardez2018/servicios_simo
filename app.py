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
      

    def find_data(self,date=None,**filters):
        if date is None:
            date = get_date()
        try:
            print(f"find data from {date}")
            return db.find_list(date,**filters)
        except db.MongoException as e:
            print(f"Exception:{e}")
            return ["epe"]
            
        
        
     

if __name__ == "__main__":
    print("Iniciando el programa")
    app = App("simo interface")
    filters = {'num': ':20230824194351.000'}
    data = app.find_data("20230824",**filters)
    for element in data:
        pprint.pprint(element)
   