# reverse array in place
def reverse(self, nums, nmin, nmax):
	mid = (nmin + nmax) // 2
	for i in range(mid - nmin):
		nums[nmin + i], nums[nmax - i - 1] = nums[nmax - i - 1], nums[nmin + i]

# rotate array in place
def rotate(self, nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	n = len(nums)
	
	m = k % n
	
	if m == 0:  # do nothing
		return
	
	self.reverse(nums, 0, n) # reverse full array
	
	self.reverse(nums, 0, m) # reverse array[:m]
	
	self.reverse(nums, m, n) # reverse array[m:]
	
	return
