import time as t
import data
import sort
import csort 


print('-----python------')

t1_insertionSort = t.time()
sort.insertionSort(data.getarray())
t2_insertionSort = t.time()
result_insertionSort_time = t2_insertionSort - t1_insertionSort
print('The time obtained for the insertion sort algorithm with python is: ', end=' ')
print(result_insertionSort_time,'\n')

t1_mergeSort = t.time()
sort.mergeSort(data.getarray())
t2_mergeSort = t.time()
print('The time obtained for the merge sort algorithm with python is: ',end=' ')
result_mergeSort_time = t2_mergeSort - t1_mergeSort
print(result_mergeSort_time,'\n')


print('Algorithm execution time ratio with python is:',round(result_insertionSort_time/result_mergeSort_time,2))


print('\n','-----Cython------','\n')

t1_CinsertionSort = t.time()
csort.c_insertionSort(data.getarray())
t2_CinsertionSort = t.time()
result_cinsertionSort_time = t2_CinsertionSort - t1_CinsertionSort
print('The time obtained for the insertion sort algorithm with Cyton is: ', end=' ')
print(result_cinsertionSort_time, '\n')


t1_CmergeSort = t.time()
csort.c_mergeSort(data.getarray())
t2_CmergeSort = t.time()
result_cmergeSort_time = t2_CmergeSort - t1_CmergeSort
print('The time obtained for the merge sort algorithm with Cyton is: ', end=' ')
print(result_cmergeSort_time,'\n')

print('Algorithm execution time ratio with Cython is:',round(result_cinsertionSort_time/result_cmergeSort_time,2))