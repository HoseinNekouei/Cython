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

#Result

-----python------
The time obtained for the insertion sort algorithm with python is:  0.2517232894897461 

The time obtained for the merge sort algorithm with python is:  0.008934497833251953

insertion sort / merge sort by Python:  28.17

 -----Cython------

The time obtained for the insertion sort algorithm with Cyton is:  0.0049991607666015625

The time obtained for the merge sort algorithm with Cyton is:  0.0030014514923095703 

insertion sort / merge sort by Cython:  1.67

#Finaly

Choosing the right algorithm and using Cython will increase the speed of code running in Python amazingly