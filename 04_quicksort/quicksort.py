def quicksort(array):
    # Check if that's the best case, it's already sorted
    if len(array) < 2:
        return array
    else:
        # Chose the first element as pivot
        pivot = array[0]
        # Divides it to two arrays, one greater and one less than the pivot
        less = [i for i in array [1: ] if i <= pivot]
        greater = [i for i in array [1: ] if i > pivot]
        # Concatenate the arrays
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([20,50,1,6,2]))
