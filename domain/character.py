from abc import ABC, abstractmethod


class Personaje(ABC):
    def __init__(self, nombre: str, vida_maxima: int, poder_ataque: int):
        self._nombre = nombre
        self._vida_maxima = vida_maxima
        self._vida = vida_maxima
        self._poder_ataque = poder_ataque

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def vida(self) -> int:
        return self._vida

    @property
    def vida_maxima(self) -> int:
        return self._vida_maxima

    @property
    def esta_vivo(self) -> bool:
        return self._vida > 0

    def recibir_dano(self, cantidad: int) -> None:
        dano = max(0, cantidad)
        self._vida = max(0, self._vida - dano)

    def curarse(self, cantidad: int) -> None:
        cura = max(0, cantidad)
        self._vida = min(self._vida_maxima, self._vida + cura)

    def ataque_basico(self, objetivo: "Personaje") -> str:
        objetivo.recibir_dano(self._poder_ataque)
        return f"{self.nombre} ataca a {objetivo.nombre} y causa {self._poder_ataque} de daño."

    @abstractmethod
    def tomar_turno(self, objetivo: "Personaje") -> str:
        pass