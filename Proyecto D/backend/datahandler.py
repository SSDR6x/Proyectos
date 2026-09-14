import json
import os

path = os.path.join("log.json")

def guadar_datos(datos: bytearray) -> json:
        
    pass

def cargar_datos(datos: bytearray) -> json:
    datos_sf = json.loads(datos)

    with open(path, "a",  encoding="utf-8") as f:
        f.writelines(datos_sf)
        pass


