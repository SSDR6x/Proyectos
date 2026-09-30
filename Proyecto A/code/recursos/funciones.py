import tkinter
from tkinter import ttk

class label_format:

    def __init__(self, texto, ubicacion, columna, fila, inclinacion):
        self.texto = texto
        self.ubicacion = ubicacion
        self.columna = int(columna)
        self.fila = int(fila)
        self.inclinacion = inclinacion

    
    def __str__(self):
        return self.texto
    

    def visible(self):
        return ttk.Label(self.ubicacion, textvariable=self.texto).grid(column=self.columna, row=self.fila, sticky=self.inclinacion)




# def new_game():
#     return continue

def close_game():
    return exit()


