# Insertion sort in Python
# Insertion Sort Complexity
# Time Complexity	 
# Best	O(n)
# Worst	O(n2)
# Average	O(n2)
# Space Complexity	O(1)
# Stability	Yes

def insertionSort(array):

    # Compare key with each element on the left of it until an element smaller than it is found
    # For descending order, change key<array[j] to key>array[j].     
    for step in range(1,len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        # Place key at after the element just smaller than it.    
        array[j + 1] = key


