# ⚔️ Combate por turnos en consola

> Challenge 1 · The Huddle · Python · Programación orientada a objetos

Juego de combate por turnos en la terminal, ambientado en un mundo de fantasía oscura. El jugador enfrenta enemigos aleatorios ronda tras ronda hasta llegar al jefe final.

## 🎮 Cómo se juega

En cada turno elegís una acción:

| Tecla | Acción |
|---|---|
| `1` | Ataque básico |
| `2` | Beber un frasco de curación (+30 de vida, 4 usos) |
| `3` | Habilidad especial: daño x2; se carga en 3 turnos |

Después de derrotar a 3 enemigos comunes aparece el jefe. Si lo vencés, ganás la partida.

## 🧱 Diseño

El proyecto separa responsabilidades en capas y usa herencia y encapsulamiento:

```text
main.py            # Punto de entrada
domain/
  character.py     # Clase base Personaje (vida, ataque, daño, curación)
  player.py        # Jugador: frascos y habilidad cargable
  enemy.py         # Enemigos comunes
  boss.py          # Jefe final
engine/game.py     # Bucle de juego, rondas y turnos
ui/console.py      # Entrada/salida por consola
```

- `Personaje` define la interfaz común (`tomar_turno`, `recibir_dano`, `curarse`) y cada subclase la especializa.
- El motor (`Juego`) no imprime nada directamente: delega toda la presentación en `ConsolaUI`.

## 🚀 Ejecutar

Requiere Python 3.10+ y no tiene dependencias externas.

```bash
python main.py
```
