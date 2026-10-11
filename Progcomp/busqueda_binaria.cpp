#include <iostream>
#include <vector>


int main(){
    
    int n, t, time_needed; //n_maquinas, productos_a_hacer, tiempo necesario por maquina para hacer producto
    std::vector<int> vector_tproduct;

    for(int i = 0; i<n; i++){
        std::cin >> time_needed;
        vector_tproduct.push_back(time_needed);
    }
    
    for (int i = 0; i<vector_tproduct.size(); i++){
        std::cout << vector_tproduct[i];
    }
    
    return 0;
}
