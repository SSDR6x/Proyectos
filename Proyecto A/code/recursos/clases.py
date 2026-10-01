from abc import ABC, abstractmethod
from random import randint, random



class Personaje(ABC):

    def __init__(self, nombre: str, vida: int, armadura: int,
                 ataque: int):
        self.nombre = nombre
        self.vida = vida
        self.armadura = armadura
        self.ataque = ataque

    @abstractmethod
    def __str__(self):
        return (f"PLAYER STATS:\n"
                f"{"_"*8}\n"
                f"NAME: {self.nombre}\n"
                f"HP: {self.vida}\n"
                f"DEF: {self.armadura}\n"
                f"ATK: {self.ataque}")
    
    @abstractmethod
    def atacar(self, objetivo: Enemigo | Jugador):
        pass

class Jugador(Personaje):
    
    def __int__(self,  nombre: str, vida: int, armadura: int,
                 ataque: int):
        super().__init__(nombre, vida, armadura, ataque)

    def __str__(self):
        return (f"PLAYER STATS:\n"
                f"{"_"*8}\n"
                f"NAME: {self.nombre}\n"
                f"HP: {self.vida}\n"
                f"DEF: {self.armadura}\n"
                f"ATK: {self.ataque}")

    def atacar(self, enemigo: Enemigo):
        enemigo.armadura

        pass

    def parry(self, objetivo: Enemigo) -> str | None:
        prob_parry = random()

        if prob_parry >= .8:
            objetivo.vida -= self.ataque*1.5
            return (f"{self.nombre} ha contrarrestrado el ataque de {objetivo.nombre}!!, "
                    f"le realiza {self.nombre} de DMG aumentado.")


class Enemigo(Personaje):

    def __init__(self,  nombre: str, vida: int, armadura: int,
                 ataque: int):
        super().__init__(nombre, vida, armadura, ataque)

    def __str__(self):
        return (f"ENEMY: {self.nombre}\n"
                f"{"_"*8}\n"
                f"HP: {self.vida}\n"
                f"DEF: {self.armadura}\n"
                f"ATK: {self.ataque}")
    
    def atacar(self, jugador: Jugador):
        crit = random.randint(1, 4)
        reduccion_dmg = jugador.armadura


        match crit:
            case 1:
                if random() == 1:
                    jugador.vida -= jugador.vida
                    return (f"Un desafortunado evento ha ocurrido, con una probabilidad"
                             "de 1/1000 tu personaje ha sido ejecutado, GG")
                
                jugador.vida -= sum((self.ataque*1.2, -(reduccion_dmg*0.1)))
                return (f"{self.nombre} ha atacado a {jugador.nombre}!!, ha sido super efectivo, "
                        f"le realizó {sum((self.ataque*1.2, -(reduccion_dmg*0.1)))} de DMG")

            case 2:
                jugador.vida -= sum((self.ataque*1.2, -(reduccion_dmg*0.2)))
                return (f"{self.nombre} ha atacado a {jugador.nombre}!!, le ha hecho" 
                        f"{((self.ataque*1.2, -(reduccion_dmg*0.2)))} de DMG")

            case 3:
                jugador.vida -= sum((self.ataque*1.2, -(reduccion_dmg*0.4)))
                return (f"{self.nombre} ha atacado a {jugador.nombre}!!, apenas le ha hecho daño, "
                        f"le realizó {sum((self.ataque*1.2, -(reduccion_dmg*0.4)))} de DMG")

            case 4:
                return (f"{self.nombre} ha atacado a {jugador.nombre}!!, {jugador.nombre} ha "
                         "esquivado el ataque")

