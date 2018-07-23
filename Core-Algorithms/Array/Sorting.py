# Small array sorting

"""
BubbleSort swap the adjacent elements which are not in order from end to start (i = 0,1,...,n-2), 
stable, worst case: time: O(n^2) space: O(1)
"""

def BubbleSort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]       
    return array

"""
SelectionSort selects the argmin of array[j:] (j = 1,...,n-1)
unstable, worst case: time: O(n^2) space: O(1)
"""
  
def SelectionSort(array):
    n = len(array)
    for i in range(n-1):
        min_ix = i
        # select argmin
        for j in range(i+1, n):
            if array[min_ix] > array[j]:
                min_ix = j
        if i != min_ix:
            array[i], array[min_ix] = array[min_ix], array[i]
    return array

"""
InsertionSort inserts array[j] into sorted sub-array array[:j] (i = 1,...,n-1)
stable, worst case: time: O(n^2) space: O(1)
"""
  
def InsertionSort(array):
    n = len(array)
    for i in range(1, n):
        tmp = array[i]
        j = i
        pre_j = j - 1
        # insert
        while j > 0 and array[pre_j] > tmp:
            array[j] = array[pre_j] 
            j = pre_j
            pre_j -= 1
        array[j] = tmp
    return array 

# large array sorting
   
"""
QuickSort divides array into two parts according to pivot element 
unstable, worst case: time: O(n^2) space: O(n log n)
"""

"""
MergeSort divides array into parts and merge them iteratively (i = 1,...,n-1)
stable, worst case: time: O(n log n) space: O(1)
"""

"""
HeapSort builds a heap and pop elements 
unstable, worst case: time: O(n log n) space: O(1)
"""
