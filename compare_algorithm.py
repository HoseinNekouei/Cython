import time as t
import data
import sort

print('-----python------')

t1_insertionSort = t.time()
sort.insertionSort(data.getarray())
t2_insertionSort = t.time()

print('Sorted Array in Ascending Order:')
print(data)

print('time of insertion sort is: ')
print(t2_insertionSort - t1_insertionSort)
