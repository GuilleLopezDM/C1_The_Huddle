import random
from domain.enemy import Enemigo
from domain.character import Personaje


class Margit(Enemigo):
    def __init__(self):
        super().__init__(nombre="Margit, el Augurio Caído", vida_maxima=100, poder_ataque=16)

    def tomar_turno(self, objetivo: Personaje) -> str:
        accion = random.choice(["ataque", "sagrado", "curar"])

        if accion == "sagrado":
            dano = self._poder_ataque + 10
            objetivo.recibir_dano(dano)
            return f"{self.nombre} invoca una daga sagrada y causa {dano} de daño."

        if accion == "curar" and self.vida <= 40:
            self.curarse(10)
            return f"{self.nombre} absorbe poder dorado y recupera 10 de vida."

        return self.ataque_basico(objetivo)