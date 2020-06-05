def selectionSort(array):
# iterate through the array
    for i in range(len(array)): 
        
        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i 
        for j in range(i+1, len(array)): 
            if array[min_idx] > array[j]: 
                min_idx = j 

        # Swap the found minimum element with  
        # the first element         
        array[i], array[min_idx] = array[min_idx], array[i] 

    for i in range(len(array)): 
        print("%d" %array[i]),  


array = [500, 110, 250, 220, 50] 

selectionSort(array);