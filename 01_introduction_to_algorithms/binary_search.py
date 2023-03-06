class BinarySearch():

    def binary_search(self,list, item):
        ## Variables to keep track of the list 
        low = 0
        high = len(list) - 1

        while(low <= high):
            ## Checking the mid element
            mid = (low + high) // 2
            guess = list[mid]
            
            ## Item found
            if guess == item:
                return mid
            
            ## Too low
            elif guess < item:
                low = mid + 1
            
            ## Too high
            else:
                high = mid - 1
            
            ## Item not found
            return None
        
    def search_recursive(self,list,item, low, high):

        ## Check base case
        if high >= low:
            
            mid = (low + high) // 2
            guess = list[mid]

            ## Item found 
            if guess == item:
                return mid
            
            ## Too low
            elif guess < item:
                return self.search_recursive(list, item, low, mid - 1)
            
            ## Too high
            else:
                return self.search_recursive(list, item, mid + 1, high)
        
        else:
            return None

my_list = [1,3,5,7,9]

bs = BinarySearch()

print(bs.binary_search(my_list,5))
print(bs.binary_search(my_list,10))
