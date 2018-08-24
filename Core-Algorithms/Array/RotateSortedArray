def biSearch(Array, target):
    left, right = 0, len(Array)-1
    while left != right:
        mid = (left + right) >> 1
        if Array[mid] < target:
            left = mid + 1
        else:
            right = mid
    if Array[left] == target:
        return left
    else:
        return -1

def minNumberIndexInRotateSortedArray(rotateSortedArray):
    left, right = 0, len(rotateSortedArray)-1
    while left != right:
        mid = (left + right) >> 1
        if rotateSortedArray[mid] > rotateSortedArray[-1]:
            left = mid + 1
        else:
            right = mid
    return left

def searchInRotateSortedArray(rotateSortedArray, target):
    if len(rotateSortedArray) == 0:
            return -1
    
    min_ix = minNumberIndexInRotateSortedArray(rotateSortedArray)
    
    if target == rotateSortedArray[-1]:
        return len(rotateSortedArray)
    elif target < rotateSortedArray[-1]:
        offset = biSearch(rotateSortedArray[min_ix:-1], target)
        if offset == -1:
            return -1
        else:
            return min_ix + offset
    else:
        return biSearch(rotateSortedArray[:min_ix], target)
