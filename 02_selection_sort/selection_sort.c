#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int findSmallest(int *arr, int size);
int *selectionSort(int *arr, int size);

int main(){
    int array[10] = {10,6,28,9,4,3,2,1,0,7};
    int size = sizeof(array)/sizeof(array[0]);
    int *sorted = selectionSort(array, size); 
    for(int i = 0; i < size; i++){
        printf("\n%d", sorted[i]);
    }
    return 0;
}

// Find the smallest value in the array
int findSmallest(int *arr, int size){
    // Store the smallest value
    int smallest = arr[0];
    // Store the index of the smallest value 
    int smallest_index = 0;
    for(int i = 1; i < size; i++){
        if(arr[i] < smallest){
            smallest = arr[i];
            smallest_index = i;
        }
    }
    return smallest_index;
}

int *selectionSort(int *arr, int size){
    // Creating a new array
    int *newarr = (int *)malloc(size*sizeof(int));
    for(int i = 0; i < size; i++){
        int smallest = findSmallest(arr, size);
        newarr[i] = arr[smallest];
        // Specifying the maximum size of the item
        arr[smallest] = INT_MAX;
    }
    return newarr;
}
