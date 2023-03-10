#include <stdio.h>

int sum(int *arr, int index, int size);

int main(){
    int arr[5] = {10,20,30,40,50};

    printf("\n%d\n",sum(arr,0, (sizeof(arr)/sizeof(arr[0]))));
}

int sum(int *arr, int index, int size){
    if (index == size){
        return 0;
    }
    return arr[index] + sum(arr,index+1, size);
}
