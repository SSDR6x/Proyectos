import requests
from flask import Flask
import socket 
import datahandler as data
import pickle
import json
import threading as tr


HOST = "localhost"
PORT = 5000

app = Flask(__name__)


@app.route("/inventario", methods=["GET"])
def obtener_inventario():
    data.
    pass

class Server():

    def __init__(self):
        self.host = HOST 
        self.port = PORT
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.socket.bind((self.host, self.port))

    def escuchar(self):    
        self.socket.listen()
        cliente, direccion = self.socket.accept()
        while True:
            thread_cliente = tr.Thread(target=self.aceptar_usuario, args=(cliente, direccion))
            thread_cliente.start()
            
    def aceptar_usuario(self, usuario: socket):
        pass
    def añadir_usuario(self):
        pass
#if __name__ == "__main__":
 #   app.run()

