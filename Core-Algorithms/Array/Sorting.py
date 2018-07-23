def swap_elem(List, i, j):
    List[i], List[j] = List[j], List[i]

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
MergeSort divides array into parts and merge them iteratively
stable, worst case: time: O(n log n) space: O(1)
"""

"""
HeapSort builds a heap and pop elements 
unstable, worst case: time: O(n log n) space: O(1)
"""
def siftup(heap, end):
    q = end
    qr = q >> 1
    
    while q > qr and heap[q] < heap[qr]:
        swap_elem(heap, q, qr)
        q = qr
        qr = q >> 1
    return

def siftdown(heap, start):
    n = len(heap)
    q = start
    
    while True:
        ql = (q - start) << 1
        rootval = heap[q]
        left_ix  = start + ql + 1
        right_ix = start + ql + 2
        
        if left_ix < n and rootval > heap[left_ix]:
            swap_elem(heap, q, left_ix)
            q = left_ix
        
        elif right_ix < n and rootval > heap[right_ix]:
            swap_elem(heap, q, right_ix)
            q = right_ix
        
        else:
            break
    return

def HeapSort(List):
    n = len(List)
    for i in range(1, n):
        siftup(List, i)
    for i in range(1, n-1):
        siftdown(List, i)
    return List
