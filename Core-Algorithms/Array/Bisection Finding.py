"""
bi_search(array, x)
:input params:
	array: ascending-order sorted, `List`
	x: `int` or `float`
:output params:
	ix: if `x` is found in array, return the first index `ix` satisfying `array[ix] == x`, else return -1
"""
def bi_search(array, x):
	nmin, nmax = 0, len(array)-1

	while nmin != nmax:
		mid = (nmin + nmax) >> 1
		if array[mid] < x:
			nmin = mid + 1
		else:
			nmax = mid
		
	if array[nmin] == x:
		return nmin
	else:
		return -1
