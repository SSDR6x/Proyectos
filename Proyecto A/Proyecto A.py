import random
# from Funciones import ataque_nulo

cont_turnos = 0


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
            return f"{self.nombre} ha atacado a {objetivo.nombre}!!, ha sido super efectivo, le realizó {int(self.ataque*1.5)} d e DMG"
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
        
    def defenderse(self, jugador):
        
        prob_defensa = random.randint(0,1)
        if prob_defensa == 1: #Como hago q funcione
            print(f"{self.nombre} se ha defendido exitosamente, el ataque es ineficaz.\nHaces 0 de DMG")
        else:
            print(f"{self.nombre} ha tratado de defenderse\n...Pero ha fallado, infringes {jugador.ataque} de DMG")
            
                

Enemigo = NPC("Saibaiman", "1000", "20", "12")

stats_J1 = str()
print("Bienvenido al entorno de pruebas, se te asignará un personaje para jugar combates uno a uno vs la computadora.")
nombre_jugador = input("Ingrese su nombre: ")

if len(nombre_jugador) == 0:
    while len(nombre_jugador) == 0:
        nombre_jugador = input("El nombre debe contener al menos 1 caracter. Ingrese un nombre valido: ")

else:
    stats_J1 = input("Ingrese las stats del personaje en el formato nombre,vida,armadura,ataque. Ten en consideración que si las stats son exageradas, se le aplicaran debuffos\n")
    
    while "," not in stats_J1:
        stats_J1 = input("Formato de ingreso incorrecto, por favor siga el formato recomendado; stat_1,stat_2,stat_n...\n")

    stats_J1 = stats_J1.split(",")

J1 = Jugador(*stats_J1)
print(J1)


print(f"Jugador {nombre_jugador} ha creado al personaje {J1.nombre} para su enfrentamiento. Su enemigo 1er enemigo es {Enemigo.nombre}.\n")
print(f"Este combate se relizará por turnos, las stats de ambos lados son las siguientes: \n{J1}\n\n{Enemigo}\n")
print(f"Cada jugador tendrá un turno para atacar, esquivar, bloquear.\nAdicionalmente, existe una probabilidad de parry (el cual aplica el mismo multiplicador que un ataque \"efectivo\")")



print("El combate da inicio.")    

while J1.vida > 0 and Enemigo.vida > 0:
    print(f"Turno/Ronda {cont_turnos}\nHP {J1.nombre}: {J1.vida} | HP {Enemigo.nombre}: {Enemigo.vida}")

    
    if cont_turnos%2 == 0:
        attr = input("Que acción deseas realizar, acciones disponibles;\nAtacar\n")
        accion = getattr(J1, attr, None)

        if attr not in ("atacar","defender"):
            for i in range(0,3):
                attr = input(f"acción invalida/incorrecta - intentos restantes: {3-(i+1)}, prueba de nuevo:\n")
                if attr in ("atacar","defender"):
                    accion = getattr(J1, attr, None)
                    break
                else: 
                    continue
        
        if attr not in ("atacar","defender"):
            print("Has acabado tus intentos disponibles, se continuará al siguiente turno.")
        else:
            print(accion(Enemigo))



    # else:

    
    cont_turnos += 1