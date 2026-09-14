#include <iostream>
#include <raylib.h>
#include <math.h>
#include <rlgl.h>
#include <vector>
#include <thread>

class Personaje{
    public:
    int HP;
    std::string nombre;
    Texture2D HeroTexture = LoadTexture("Resources/Textures/BSquare.png");
    
    void moverPersonaje(char direccion){
        switch (direccion){
            case 'w':
            posY -= 1; 
            break;
            case 's':
            posY += 1;
            break;
            case 'a':
            posX -= 1;
            break;
            case 'd':
            posX += 1;
            break;
        }
    }
    void detectarColision(std::vector<int> mallaColisionEnemigo){
    
    }
    void dibujarPersonaje(){
        DrawTexture(HeroTexture, posX, posY, WHITE);
    }
    private:
        int id;
        int posX = 320;
        int posY = 240;
        int filas = 40;
        int columnas = 40;
        int valorInicial = 0;
        std::vector<std::vector<int>>mallaColision(filas, std::vector<int>(columnas, valorInicial));
};

class Enemigo{
    public: 
        std::string nombre;

    private:
        int posX;
        int posY;
        int HP;

};
int main(){
    Color backgroundColor = {255, 255, 255, 255};
    InitWindow(640, 480,  "Try");
    SetTargetFPS(60);
    Personaje Hero;
        
    while (!WindowShouldClose()){
        BeginDrawing(); //call  para empezar a dibujar
        ClearBackground(backgroundColor);
        Hero.dibujarPersonaje();
        
        if (IsKeyDown(KEY_W)){
            Hero.moverPersonaje('w');
        }
        else if(IsKeyDown(KEY_S)){
            Hero.moverPersonaje('s');
        }
        else if (IsKeyDown(KEY_D)){
            Hero.moverPersonaje('d');
        }
        else if(IsKeyDown(KEY_A)){
            Hero.moverPersonaje('a');
        }
        EndDrawing();
        }
    return 0;
    }