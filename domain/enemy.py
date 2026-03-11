import random
from domain.character import Personaje


class Enemigo(Personaje):
    def __init__(self, nombre: str, vida_maxima: int, poder_ataque: int):
        super().__init__(nombre=nombre, vida_maxima=vida_maxima, poder_ataque=poder_ataque)

    def tomar_turno(self, objetivo: Personaje) -> str:
        return self.ataque_basico(objetivo)


class SoldadoDeGodrick(Enemigo):
    def __init__(self):
        super().__init__(nombre="Soldado de Godrick", vida_maxima=60, poder_ataque=12)

    def tomar_turno(self, objetivo: Personaje) -> str:
        if random.random() < 0.30:
            dano = self._poder_ataque + 8
            objetivo.recibir_dano(dano)
            return f"{self.nombre} realiza un golpe pesado y causa {dano} de daño."
        return self.ataque_basico(objetivo)


class DemiHumano(Enemigo):
    def __init__(self):
        super().__init__(nombre="Demi-Humano", vida_maxima=70, poder_ataque=14)

    def tomar_turno(self, objetivo: Personaje) -> str:
        dano_por_golpe = self._poder_ataque // 2
        dano_total = dano_por_golpe * 2

        for _ in range(2):
            objetivo.recibir_dano(dano_por_golpe)

        return f"{self.nombre} ataca salvajemente dos veces y causa {dano_total} de daño total."