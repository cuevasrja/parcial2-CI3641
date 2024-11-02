#include <iostream>

int f(int n){
    if (n % 2 == 0){
        return n/2;
    } 
    return 3*n + 1;
}

int main(int argc, char const *argv[])
{
    if (argc != 2){
        return 1;
    }

    int n = atoi(argv[1]);
    int count = 0;

    while (n != 1){
        n = f(n);
        count++;
    }

    printf("Number of iterations: \033[93;1m%d\033[0m\n", count);
    
    return 0;
}
