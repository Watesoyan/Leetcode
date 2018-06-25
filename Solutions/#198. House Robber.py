class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        G[i] = max(G[i-1], G[i-2]+nums[i]), G[-1] = 0, G[-2] = 0
        """
        n = len(nums)
        
        if n == 0:
            return 0
        
        a = b = 0
        
        for i in range(n):
            b, a = max(a + nums[i], b), b
        
        return b
