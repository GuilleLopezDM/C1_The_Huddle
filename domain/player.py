from domain.character import Personaje


class Sinluz(Personaje):
    def __init__(self, nombre: str):
        super().__init__(nombre=nombre, vida_maxima=120, poder_ataque=22)
        self._frascos = 4
        self._carga_ceniza = 0

    @property
    def frascos(self) -> int:
        return self._frascos

    @property
    def carga_ceniza(self) -> int:
        return self._carga_ceniza

    def beber_frasco(self) -> str:
        if self._frascos <= 0:
            return f"{self.nombre} no tiene Frascos de Lágrimas Carmesí."
        self._frascos -= 1
        self.curarse(30)
        return f"{self.nombre} bebe un Frasco de Lágrimas Carmesí y recupera 30 de vida."

    def cargar_ceniza(self) -> None:
        self._carga_ceniza = min(3, self._carga_ceniza + 1)

    def usar_ceniza_de_guerra(self, objetivo: Personaje) -> str:
        if self._carga_ceniza < 3:
            return "La Ceniza de Guerra todavía no está lista."
        dano = self._poder_ataque * 2
        objetivo.recibir_dano(dano)
        self._carga_ceniza = 0
        return f"{self.nombre} usa una Ceniza de Guerra sobre {objetivo.nombre} y causa {dano} de daño."

    def tomar_turno(self, objetivo: Personaje) -> str:
        return self.ataque_basico(objetivo)