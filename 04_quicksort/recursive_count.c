#include <stdio.h>

int count(int *arr, int index, int size);

int main(){
    int arr[5] = {10,20,30,40,50};

    printf("\n%d\n",count(arr,0, (sizeof(arr)/sizeof(arr[0]))));
}

int count(int *arr, int index, int size){
    if (index == size){
        return 0;
    }
    return 1 + count(arr,index+1, size);
}
