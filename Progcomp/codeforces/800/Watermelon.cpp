#include <bits/stdc++.h>

int main(){

    int w;

    std::cin >> w;

    for(int i = 0; i < 100; i++){
        for(int j = 0; j < 100; j++){
            if((i % 2 == 0 && j % 2 == 0) && (i != 0 && j != 0) && i + j == w){
                std::cout << "YES";
                return 0;
            }
        }
        
    }
    std::cout << "NO";
    return 0;
}