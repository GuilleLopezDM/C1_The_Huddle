class ConsolaUI:
    def mostrar_mensaje(self, mensaje: str) -> None:
        print(mensaje)

    def mostrar_estado(self, jugador, enemigo) -> None:
        print("\n" + "-" * 60)
        print(
            f"Jugador: {jugador.nombre} | "
            f"Vida: {jugador.vida}/{jugador.vida_maxima} | "
            f"Frascos: {jugador.frascos} | "
            f"Ceniza: {jugador.carga_ceniza}/3"
        )
        print(
            f"Enemigo: {enemigo.nombre} | "
            f"Vida: {enemigo.vida}/{enemigo.vida_maxima}"
        )
        print("-" * 60)

    def pedir_accion(self) -> str:
        print("\nElegí una acción:")
        print("1. Atacar")
        print("2. Beber frasco")
        print("3. Usar Ceniza de Guerra")
        return input("> ").strip()

    def mostrar_fin_del_juego(self, victoria: bool) -> None:
        if victoria:
            print("\n¡Victoria! El Sinluz ha prevalecido en las Tierras Intermedias.")
        else:
            print("\nHas caído en combate. La gracia te ha abandonado.")