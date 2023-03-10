#include <stdio.h>

int fat(int x);

int main(){
    printf("\n%d\n", fat(5));
}

int fat(int x){
    if(x == 1){
        return 1;
    }
    else{
        return x * fat(x-1);
    }
}
