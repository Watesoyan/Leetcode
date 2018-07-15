"""
bisect_find(array, x)
:input params:
	array: ascending-order sorted, `List`
	x: `int` or `float`
:output params:
	ix: if x is found in array, return small index ix satisfying array[ix] == x, else return -1
"""
def bisect_find(array, x):
	n = len(array)
	nmin, nmax = 0, n-1

	while nmin != nmax:
		mid = (nmin + nmax) // 2
		if array[mid] < x:
			nmin = mid + 1
		else:
			nmax = mid
		
	if array[nmin] == x:
		return nmin
	else:
		return -1
