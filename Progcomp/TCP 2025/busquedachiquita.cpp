#include <iostream>
#include <vector>
#include <bits/stdc++.h>


int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::vector<int> alturas;
    int n, q;
    int altura;

    std::cin >> n >> q;
   
    for(int i = 0; i < n; i++){
        std::cin >> altura;
        alturas.push_back(altura);
    }
    std::sort(alturas.begin(), alturas.end());

    int q_altura;

    for(int i = 0; i < q; i++){
        int l = 0, r = n - 1;
    
        std::cin >> q_altura;
        
        if(n == 0 || alturas[n-1] < q_altura){
            std::cout << n << "\n";
            continue;
        }
        
        while(l != r){
            int mid = (l + r)/2;
            
            if(alturas[mid] >= q_altura){
                r = mid;
            } 
            else{
                l = mid + 1;
            }
            
        }    
        if(alturas[l] >= q_altura){
            std::cout << l << "\n";
        }   
    }
    return 0;
}