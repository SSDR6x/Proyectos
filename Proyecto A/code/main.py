from raylib import *
from recursos.clases import Jugador, Enemigo


if __name__ == "__main__":
    InitWindow(800, 600, b"Proyecto A")

    while not WindowShouldClose():
        BeginDrawing()
        ClearBackground(WHITE)
        DrawText(b"Hola", 400, 400, 20, BLACK)
        
        match        
        EndDrawing()
    CloseWindow()