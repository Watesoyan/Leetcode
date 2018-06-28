class Solution:
    # takes 76 ms in LeetCode benchmark
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        
        if n <= 2:
            return 0
        
        longest = 0
        flag1 = 0                            # set flag when going up 
        flag2 = 0                            # set flag when going down after going up 
        
        for i in range(n - 1):
            d = A[i] - A[i+1]
            
            if flag2 == 1 and d <= 0:        # down->
                right = i
                tmp = right - left + 1       # calculate the length of mountain
                if tmp > longest:
                    longest = tmp
                flag2 = 0
            if flag1 == 0: 
                if d < 0:                    # ->up
                    left = i
                    flag1 = 1
            else:
                if d > 0:                    # up->peak->down
                    flag1 = 0
                    flag2 = 1
                if d == 0:                   # up->peak->flat
                    flag1 = 0
        
        if flag2 == 1:
            right = n-1
            tmp = right - left + 1       # calculate the length of mountain
            if tmp > longest:
                longest = tmp
        
        return longest
