class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        # [] # # # # # #
           k   i     j        
        
        """
        n = len(nums)
        
        if n <= 1:
            return n
        
        i = k = 0
        j = 1
        
        while i < n:
            
            if j < n and nums[i] == nums[j]:
                j += 1
            else:
                nums[k] = nums[i]
                k += 1
                i = j
                j += 1
                
        return k
