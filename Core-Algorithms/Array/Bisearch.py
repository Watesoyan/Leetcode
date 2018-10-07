"""
bi_search(array, x)
:input params:
    array: ascending-order sorted, `List`
    x: `int` or `float`
:output params:
    ix: if `x` is found in array, return the first index `ix` satisfying `array[ix] == x`, else return -1
"""
def bisearch(arr, x):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r) >> 1
        if arr[mid] < x:
            l = mid + 1
        else:
            r = mid
    return l if arr[l] == x else -1
