#include <bits/stdc++.h>

int main(){

    int n, p, v, t;
    int problemas_resueltos = 0;

    std::cin >> n;

    for(int i = 0; i < n; i++){
        std::cin >> p >> v >> t;
        if(p + v + t >= 2){
            problemas_resueltos += 1;
        }
    }

    std::cout << problemas_resueltos;

    return 0;
}
