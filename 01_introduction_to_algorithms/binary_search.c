#include <stdio.h>

int binary_search(int list[], int item, int len);

int main(){
    int list[] = {0,1,2,3,4};
    int len = sizeof(list)/sizeof(list[0]);;
    
    printf("\n%d\n", binary_search(list,3,len));
}

int binary_search(int list[],int item, int len){
    int low = 0;
    int high = len;

    while(low <= high){
        int mid = (low + high) / 2;
        int guess = list[mid];

        if(guess == item){
            return mid;
        }

        else if(guess < item){
            low = mid + 1;
        }

        else{
            high = mid - 1;
        }
    }

    return -1;
}
