 #include <bits/stdc++.h>

 int main(){

    int n;
    std::string word;

    std::cin >> n;

    for(int i = 0; i < n; i++){
        std::cin >> word;
        if(word.length() > 10){
            std::cout << word[0] << (word.length() - 2) << word.back() << std::endl;
        }
        else{
           std::cout << word << std::endl;
        }
    }
    return 0;
 }