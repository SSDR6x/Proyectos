import random
# import pygame
import tkinter as tk
from tkinter import ttk
from Funciones import label_format
from Funciones import close_game

# from pkg_resources import resource_stream, resource_exists

#pygame para el build 2d


#Apertura y formateo de documentos
NPCs = open("NPCs.txt",'r')
Texto_Inicial = open("Texto.txt", "r", encoding= "utf-8")
NPCs_no_formateados = str(NPCs.readlines())
Texto_no_formateado = str(Texto_Inicial.readlines())
#Cierre de archivos
NPCs.close()
Texto_Inicial.close()

#inicio de formateo
NPCs_no_formateados = NPCs_no_formateados.strip("[]").strip().strip("'").split(";")
NPCs_formateados = []




# for x in range(len(Texto_no_formateado)):
#     Texto_no_formateado[x] = Texto_no_formateado[x].strip("'").strip("\ n', ").split("|")
#     Texto_formateado.append(Texto_no_formateado[x])

# for w in range(len(Texto_formateado)):
#     Texto_formateado[w] = Texto_formateado[w][-1] 

#     print(Texto_formateado[w])

# for w in range(len(Texto_formateado)):
#     print(Texto_formateado[w])
# Texto_no_formateado = Texto_no_formateado


for i in range(len(NPCs_no_formateados)):
    NPCs_no_formateados[i] = NPCs_no_formateados[i].split(",")
    NPCs_formateados.append(NPCs_no_formateados[i])
# from Funciones import ataque_nulo

cont_turnos = 0

#interfaz grafica

# class tkinter.Tk(screenName=None, baseName=None, className='Tk', useTk=True, sync=False, use=None):

root = tk.Tk()
root.title("Proyecto A")
root.geometry("800x600")
root.minsize(720, 480)


mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(sticky=("N", "W", "E", "S"))
root.columnconfigure(0, weight=1, minsize=100)
root.rowconfigure(0, weight=1, minsize=100)



ttk.Label(mainframe, text="Bienvenido al juego", justify="center").grid(column=6,row=1)
ttk.Button(mainframe, text="Nueva Partida").grid(column=2, row=2)
ttk.Button(mainframe, text="Salir del Juego", command=close_game).grid(column=3, row=2)
ttk.Button(mainframe, text="Continuar Partida").grid(column=4, row=2)





# ttk.Label(mainframe, text=Texto_no_formateado).grid(column=2, row=2, sticky="W")



class Jugador:

    def __init__(self, nombre, vida, armadura, ataque):
        self.nombre = nombre
        self.vida = int(vida)
        self.armadura = int(armadura)
        self.ataque = int(ataque)


    def __str__(self):
        return f"\nPlayer stats:\n_________\nNombre: {self.nombre}\nHP: {self.vida}\nARMOR: {self.armadura}\nATK: {self.ataque}"
    

    def atacar(self, objetivo):
        crit = random.randint(0,10)
        reduccion_de_DMG = objetivo.armadura
        if crit >= 7:
            objetivo.vida -= int(self.ataque*1.5) - int(reduccion_de_DMG*0.1)
            return f"{self.nombre} ha atacado a {objetivo.nombre}!!, ha sido super efectivo, le realizó {int(self.ataque*1.5) - int(reduccion_de_DMG*0.1)} de DMG"
        elif crit >= 3:
            objetivo.vida -= int(self.ataque) - int(reduccion_de_DMG*0.2)
            return f"{self.nombre} ha atacado a {objetivo.nombre}!!, le ha hecho {int(self.ataque)- int(reduccion_de_DMG*0.2)} de DMG"
        elif crit >= 1:
            objetivo.vida -= int(self.ataque*0.2) - int(reduccion_de_DMG*0.4)
            return f"{self.nombre} ha atacado a {objetivo.nombre}!!, apenas le ha hecho daño, le realizó {int(self.ataque*0.2) - int(reduccion_de_DMG*0.4)} de DMG"
        else:
            return f"{self.nombre} ha atacado a {objetivo.nombre}!!, {objetivo.nombre} ha esquivado el ataque"

    def parry(self, objetivo):
        prob_parry = random.randint(0,5)
        if prob_parry >= 4:
            self.vida += objetivo.ataque
            objetivo.vida -= self.ataque*1.5
            return f"{self.nombre} ha contrarrestado el ataque de {objetivo.nombre}!!, le realiza {self.ataque*1.5} de DMG aumentado"

stats_J1 = str()
print("Bienvenido al entorno de pruebas, se te asignará un personaje para jugar combates uno a uno vs la computadora.")
nombre_jugador = input("Ingrese su nombre: ")

while len(nombre_jugador) == 0:
    nombre_jugador = input("El nombre debe contener al menos 1 caracter. Ingrese un nombre valido: ")

stats_J1 = input("Ingrese las stats del personaje en el formato nombre,vida,armadura,ataque. Ten en consideración que si las stats son exageradas, se le aplicaran debuffos\n")
    
while "," not in stats_J1:
    stats_J1 = input("Formato de ingreso incorrecto, por favor siga el formato recomendado; stat_1,stat_2,stat_n...\n")

stats_J1 = stats_J1.split(",")

J1 = Jugador(*stats_J1)
print(J1)

class NPC: 

    def __init__(self, nombre, vida, armadura, ataque,nivel, jugador):
        jugador = J1
        self.nombre = nombre
        self.vida = int(vida)
        self.armadura = int(armadura)
        self.ataque = int(ataque)
        self.nivel = int(nivel)
        self.J1 = jugador
       
        if self.J1.vida >= (self.vida*2):
            self.ataque = int(ataque)*2
        elif self.J1.ataque >= (self.vida)//2:
            self.armadura = int(armadura)*4


    def __str__(self):
        return f"NPC stats:\n_________\nHP: {self.vida}\nARMOR: {self.armadura}\nATK: {self.ataque}"
    
    def atacar(self, jugador):
        crit = random.randint(0,10)
        reduccion_de_DMG = jugador.armadura

        if crit >= 7:
            oneshot = random.randint(0,100)
            if oneshot == 100:
                jugador.vida -= jugador.vida
                return f"Un desafortunado evento ha ocurrido, con una probabilidad de 1/1000 tu personaje ha sido ejecutado, GG"
            else:    
                jugador.vida -= int(self.ataque*1.2) - (int(reduccion_de_DMG)*0.1)
                return f"{self.nombre} ha atacado a {jugador.nombre}!!, ha sido super efectivo, le realizó {int(self.ataque*1.2) - (int(reduccion_de_DMG)*0.1)} de DMG"
            
        elif crit < 7 and crit >= 3:
            jugador.vida -= int(self.ataque) - (int(reduccion_de_DMG)*0.2)
            return f"{self.nombre} ha atacado a {jugador.nombre}!!, le ha hecho {int(self.ataque) - (int(reduccion_de_DMG)*0.2)} de DMG"
        elif crit <3 and crit >= 1:
            jugador.vida -= int(self.ataque*0.4) - (int(reduccion_de_DMG)*0.4)
            return f"{self.nombre} ha atacado a {jugador.nombre}!!, apenas le ha hecho daño, le realizó {int(self.ataque*0.4) - (int(reduccion_de_DMG)*0.4)} de DMG"
        else:
            return f"{self.nombre} ha atacado a {jugador.nombre}!!, {jugador.nombre} ha esquivado el ataque"
        
    def defenderse(self, jugador):
        
        prob_defensa = random.randint(0,1)
        if prob_defensa == 1: #Como hago q funcione
            # self.vida += jugador.atacar #No se puede llamar directo al metodo, alguna forma de indexar el daño especifico que hace J1 para nulificarlo
            return (f"{self.nombre} se ha defendido exitosamente, el ataque es ineficaz.\nHaces 0 de DMG")
        else:
            return (f"{self.nombre} ha tratado de defenderse\n...Pero ha fallado, infringes {jugador.ataque} de DMG")


Enemigo = NPC(*NPCs_formateados[0])

print(f"Jugador {nombre_jugador} ha creado al personaje {J1.nombre} para su enfrentamiento. Su 1er enemigo es {Enemigo.nombre}.\n")
print(f"Este combate se relizará por turnos, las stats de ambos lados son las siguientes: \n{J1}\n\n{Enemigo}\n")
print(f"Cada jugador tendrá un turno para atacar, esquivar, bloquear.\nAdicionalmente, existe una probabilidad de parry (el cual aplica el mismo multiplicador que un ataque \"efectivo\")")

print("El combate da inicio.")    

cont_enemigos = 0
#Combate
while True: 
    print(f"Turno/Ronda {cont_turnos}\nHP {J1.nombre}: {J1.vida} | HP {Enemigo.nombre}: {Enemigo.vida}")
    vida_en_actual = Enemigo.vida
    rest_vida = 0
    
    if cont_turnos%2 == 0:
        attr = input("Que acción deseas realizar, acciones disponibles;\nAtacar\n")
        accion = getattr(J1, attr, None)

        if attr not in ("atacar","defender"):
            for i in range(0,3):
                attr = input(f"acción invalida/incorrecta - intentos restantes: {4-(i+1)}, prueba de nuevo:\n")
                if attr in ("atacar","defender","Atacar","Defender"):
                    accion = getattr(J1, attr)
                    break
                else: 
                    continue
                       
        if attr not in ("atacar","defender"):
            print("Has acabado tus intentos disponibles, se continuará al siguiente turno.")

        else:
            print(accion(Enemigo))
            if Enemigo.vida < vida_en_actual:
                rest_vida = vida_en_actual - Enemigo.vida
            
    #Accion NPC
    else:
        accion_npc = random.randint(0,1)
        if  accion_npc == 1:
            attr = "atacar"
            accion = getattr(Enemigo, attr)
            print(accion(J1))
        else:
            attr = "defenderse"
            accion = getattr(Enemigo, attr)
            print(accion(J1))
            #Ver como hacer que dependa del randint de defender para que no recupere si o si, solo en el caso de un bloqueo perfecto

    if J1.vida <= 0:
        break
    elif Enemigo.vida <= 0:
        if cont_enemigos == 6:
            break
        cont_enemigos += 1
        Enemigo = NPC(*NPCs_formateados[cont_enemigos])

        
    cont_turnos += 1


if J1.vida <= 0:
    print(f"Has perdido, tu personaje {J1.nombre} ha muerto.\n\nGAME OVER")

else:
    print(f"Felicidades {nombre_jugador}!! Has ganado contra todos los Enemigos dispuestos por este juego.\nGracias por probar el juego")



input("Presiona cualquier tecla para salir...")

    