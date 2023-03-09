# Find the smallest elemento in the array
def findSmallest(arr):
    # Stores the smallest element
    smallest = arr[0]
    # Stores the index of the smallest element
    smallest_index = 0

    for i in range(1,len(arr)):
        if(arr[i] < smallest):
            smallest_index = i
            smallest = arr[i]
    
    return smallest_index

# Sort arrays
def selectionSort(arr):
    newArray = []
    for i in range(len(arr)):
        # Find the smallest element and stores it to the new array
        smallest = findSmallest(arr)
        newArray.append(arr.pop(smallest))
    return newArray


print(selectionSort([10,5,2,8,4,3]))
