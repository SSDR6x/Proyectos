import random
# from Funciones import ataque_nulo




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
        if crit >= 7:
            objetivo.vida -= int(self.ataque*1.5)
            return f"{self.nombre} ha atacado a {objetivo.nombre}!!, ha sido super efectivo, le realizó {int(self.ataque*1.5)} de DMG"
        elif crit < 7 and crit >= 3:
            objetivo.vida -= int(self.ataque)
            return f"{self.nombre} ha atacado a {objetivo.nombre}!!, le ha hecho {int(self.ataque)} de DMG"
        elif crit <3 and crit >= 1:
            objetivo.vida -= int(self.ataque*0.2)
            return f"{self.nombre} ha atacado a {objetivo.nombre}!!, apenas le ha hecho daño, le realizó {int(self.ataque*0.2)} de DMG"
        else:
            return f"{self.nombre} ha atacado a {objetivo.nombre}!!, {objetivo.nombre} ha esquivado el ataque"

    def parry(self, objetivo):
        prob_parry = random.randint(0,5)
        if prob_parry >= 4:
            self.vida += objetivo.ataque
            objetivo.vida -= self.ataque*1.5
            return f"{self.nombre} ha contrarrestado el ataque de {objetivo.nombre}!!, le realiza {self.ataque*1.5} de DMG aumentado"

class NPC:

    def __init__(self, nombre, vida, armadura, ataque):
        self.nombre = nombre
        self.vida = int(vida)
        self.armadura = int(armadura)
        self.ataque = int(ataque)

    def __str__(self):
        return f"NPC stats:\n_________\nHP: {self.vida}\nARMOR: {self.armadura}\nATK: {self.ataque}"
    
    def atacar(self, jugador):
        crit = random.randint(0,10)
        if crit >= 7:
            jugador.vida -= int(self.ataque*1.2)
            return f"{self.nombre} ha atacado a {jugador.nombre}!!, ha sido super efectivo, le realizó {int(self.ataque*1.2)} de DMG"
        elif crit < 7 and crit >= 3:
            jugador.vida -= int(self.ataque)
            return f"{self.nombre} ha atacado a {jugador.nombre}!!, le ha hecho {int(self.ataque)} de DMG"
        elif crit <3 and crit >= 1:
            jugador.vida -= int(self.ataque*0.4)
            return f"{self.nombre} ha atacado a {jugador.nombre}!!, apenas le ha hecho daño, le realizó {int(self.ataque*0.4)} de DMG"
        else:
            return f"{self.nombre} ha atacado a {jugador.nombre}!!, {jugador.nombre} ha esquivado el ataque"


    
Enemigo = NPC("Saibaiman", "1000", "20", "12")


# print(f"{J1}\n\n{Enemigo} ")
# print(J1.atacar(Enemigo))

print("Bienvenido al entorno de pruebas, se te asignará un personaje para jugar combates uno a uno vs la computadora.")
nombre_jugador = input("Ingrese su nombre: ")
stats_J1 = input("Ingrese las stats del personaje en el formato nombre,vida,armadura,ataque. Ten en consideración que si las stats son exageradas, se le aplicaran debuffos\n")

stats_J1 = stats_J1.split(",")

J1 = Jugador(stats_J1)
print(J1)


# print(f"Jugador {nombre_jugador}, se le ha asignado el personaje {J1.nombre} para su enfrentamiento. Su enemigo es {Enemigo.nombre}")
# print(f"Este combate se relizará por turnos, las stats de ambos lados son las siguientes: \n{J1}\n\n{Enemigo}")
# print(f"Cada jugador tendrá un turno para atacar, esquivar, bloquear.\n\nAdicionalmente, existe una probabilidad de parry (el cual aplica el mismo multiplicador que un ataque \"efectivo\")")
# cont_turnos = 0

# while True:
    

# print(J1.atacar(Enemigo))