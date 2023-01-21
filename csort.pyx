# Insertion sort in Python
# Time Complexity
# Best	O(n)
# Worst	O(n2)
# Average	O(n2)

cpdef c_insertionSort(array):
    # Compare key with each element on the left of it until an element smaller than it is found
    # For descending order, change key<array[j] to key>array[j].
    cdef int step,j = 0
    cdef float key =0.0

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key


# Merge Sort in Python
# Time Complexity
# Best Case Complexity: O(n*log n)
# Worst Case Complexity: O(n*log n)
# Average Case Complexity: O(n*log n)

cpdef c_mergeSort(array):
    cdef int i,j,k = 0

    if len(array) > 1:

        # r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1