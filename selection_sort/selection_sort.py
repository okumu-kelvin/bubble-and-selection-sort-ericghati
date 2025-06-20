def selection_sort(arr):

    size =  len(arr)

    for i in range(size):
         min_index = i

         for num  in range(i + 1, size):
              #select the minimum element in each iteration
              if arr[num] < arr[min_index]:
                   min_index = num

            #swapping  the elements to sort the array
         (arr[i], arr[min_index]) = (arr[min_index], arr[i])

    return(arr)

arr = [-5, 6, 77, 606, -34, 90]
selection_sort(arr)
print(f"Sorted array: {arr}")
    

    
    
