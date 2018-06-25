class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n <= 1:
            return n
        
        pre = {x : x for x in nums}
        nxt = {x : x for x in nums}  
        visited = {x: 0 for x in nums} 
        
        # build sets
        for i in range(n - 1):
            if nums[i] > nums[i + 1] and  nums[i] - nums[i + 1] == 1:
                pre[nums[i]] = nums[i + 1]
                nxt[nums[i + 1]] = nums[i]
            elif nums[i] < nums[i + 1] and  nums[i] - nums[i + 1] == 1:
                pre[nums[i + 1]] = nums[i]
                nxt[nums[i]] = nums[i + 1]
            else:
                if pre.has_key(nums[i] - 1):
                    pre[nums[i]] = nums[i] - 1
                    nxt[nums[i] - 1] = nums[i]
                if pre.has_key(nums[i] + 1):
                    pre[nums[i] + 1] = nums[i]
                    nxt[nums[i]] = nums[i] + 1
        
        maxlength = 1
        
        # find max length
        for x in nums:
            if not visited[x]:
                tmp1 = tmp2 = x
                while pre[tmp1] != tmp1:
                    tmp1 = pre[tmp1]
                while nxt[tmp2] != tmp2:
                    tmp2 = nxt[tmp2]
                for y in range(tmp1, tmp2+1):
                    visited[y] = 1
                maxlength = max(tmp2 - tmp1 + 1, maxlength)
        
        return maxlength
