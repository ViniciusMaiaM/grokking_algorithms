#include <stdio.h>

void quick_sort(int *array, int start, int end);
int partition(int *array, int start, int end);

int main(){
    int arr[] = {25,40,55,20,44,35,38,99,10,65,50};
    int size = sizeof(arr)/sizeof(arr[0]);

    quick_sort(arr,0, size-1);
    printf("\n");

    for(int i = 0; i < size; i++){
        printf("%d ", arr[i]);
    }

    return 0;
}

void quick_sort(int *array, int start, int end){

    if (start < end){
        int q = partition(array, start, end);
        //Recursives calls of the function
        quick_sort(array, start, q - 1);
        quick_sort(array, q + 1, end);
    }
    
}

int partition(int *array, int start, int end){
    int pivot = array[end]; //Pivot is the last element
    int index = start;
    int aux = 0;

    for(int i = start; i < end; i++){

        //Verifying if the element is smaller than pivot
        if(array[i] <= pivot){
            //Changes the elements
            aux = array[i];
            array[i] = array[index];
            array[index] = aux;
            //Increments the pivot
            index++;
        }
    }

    //Changes pivot
    aux = array[index];
    array[index] = array[end];
    array[end] = aux;

    //Returns the pivot index
    return index;
}
