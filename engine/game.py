import random
from domain.player import Sinluz
from domain.enemy import SoldadoDeGodrick, DemiHumano
from domain.boss import Margit
from ui.console import ConsolaUI


class Juego:
    def __init__(self):
        self._ui = ConsolaUI()
        self._jugador = Sinluz("Sinluz")
        self._ronda = 1
        self._enemigos_derrotados = 0
        self._enemigo_actual = self._crear_enemigo()

    def _crear_enemigo(self):
        if self._enemigos_derrotados >= 3:
            return Margit()
        return random.choice([SoldadoDeGodrick(), DemiHumano()])

    def _manejar_accion_jugador(self, accion: str) -> str:
        self._jugador.cargar_ceniza()

        if accion == "1":
            return self._jugador.tomar_turno(self._enemigo_actual)
        elif accion == "2":
            return self._jugador.beber_frasco()
        elif accion == "3":
            return self._jugador.usar_ceniza_de_guerra(self._enemigo_actual)

        return "Acción inválida. Perdés el turno."

    def _turno_enemigo(self) -> str:
        if self._enemigo_actual.esta_vivo:
            return self._enemigo_actual.tomar_turno(self._jugador)
        return f"{self._enemigo_actual.nombre} ya no puede actuar."

    def _verificar_derrota_enemigo(self) -> bool:
        if not self._enemigo_actual.esta_vivo:
            self._ui.mostrar_mensaje(f"{self._enemigo_actual.nombre} fue derrotado.")
            self._enemigos_derrotados += 1

            if self._enemigos_derrotados >= 4:
                return True

            self._enemigo_actual = self._crear_enemigo()
            self._ronda += 1
            self._ui.mostrar_mensaje(f"\n--- Ronda {self._ronda} ---")

        return False

    def ejecutar(self):
        self._ui.mostrar_mensaje("=== La Travesía del Sinluz ===")
        self._ui.mostrar_mensaje("Levantate, Sinluz, y abríte paso por las Tierras Intermedias.\n")

        while self._jugador.esta_vivo:
            self._ui.mostrar_estado(self._jugador, self._enemigo_actual)

            accion = self._ui.pedir_accion()
            resultado_jugador = self._manejar_accion_jugador(accion)
            self._ui.mostrar_mensaje(resultado_jugador)

            if self._verificar_derrota_enemigo():
                self._ui.mostrar_fin_del_juego(victoria=True)
                return

            resultado_enemigo = self._turno_enemigo()
            self._ui.mostrar_mensaje(resultado_enemigo)

            if not self._jugador.esta_vivo:
                self._ui.mostrar_fin_del_juego(victoria=False)
                return