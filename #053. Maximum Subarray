class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        tmpsum = max(nums[0], 0)
        maxsum = nums[0]
        
        for i in range(1,n):
            tmpsum += nums[i]
            maxsum = max(tmpsum, maxsum)
            tmpsum = max(tmpsum, 0)
            
        return maxsum    
