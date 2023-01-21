# cython 

Let you know that I while Learning Cython, I compared the running time between of insertion and merge sort algorithms.

if we ignore the time complexity of merge-sort algorithm, even though it is better than insertion-sort algorithm, the results of this comparison between python and Cython are as bellow:

--
# Merge Sort Time Complexity

 Best Case Complexity: O(n*log n)

 Worst Case Complexity: O(n*log n)

 Average Case Complexity: O(n*log n)

--
# Insertion sort Time Complexity

 Best Case Complexity: O(n)

 Worst Case Complexity:	O(n2)

 Average Case Complexity: O(n2)

time of insertion sort for 2000 float number in a array is:  0.34029459953308105

time of merge sort for 2000 float number in a array is:  0.011481523513793945

That means #mergeSort algorithm is 32 times faster than #insertionSort in python