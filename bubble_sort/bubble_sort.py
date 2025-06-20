def bubble_sort(unsorted_list):

    #loop to iterate through the list of n number of elements.
    for n in range(len(unsorted_list) - 1, 0, -1):

        #we initialize a swapped to track and ensure the swaps occur as we organize the list
        swapped = False

        #loop to compare adjacent elements
        for i in range(n):
            if unsorted_list[i] > unsorted_list[i + 1]:

                #swapping the elements if they are in the wrong order
                (unsorted_list[i], unsorted_list[i+1]) = (unsorted_list[i+1], unsorted_list[i])

                #track that a swap has happened
                swapped = True

            #if no swapps happened, the list is already sorted
        if not swapped:
            break

                
    return unsorted_list 

#Testing with a sample list
unsorted_list = [8,5,6]   
bubble_sort(unsorted_list)
print(f"Sorted list: {unsorted_list}")



