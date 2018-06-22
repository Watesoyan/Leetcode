class Solution(object):
    def bisect_find(self, nums1, m, nums2, n):
        idxs = [0]*n
        m_min, m_max = 0, m
    
        for i in range(n):
            
            while m_min != m_max:
                
                mid = (m_min + m_max) // 2
                
                if nums1[mid] < nums2[i]:
                    m_min = mid + 1
                else:
                    m_max = mid
            
            idxs[i] = m_min
            
            m_max = m            # reset m_max
            
        return idxs
    
    def insert(self, nums1, m, nums2, n, idxs): # insert nums2 into nums1
        offsets = self.bisect_find(idxs, n, list(range(1,m+1)), m)
        
        for i in range(m):
            j = m - i - 1
            if offsets[j] != 0:
                nums1[j + offsets[j]] = nums1[j]   # move element to right
        
        for i in range(n):                         # replace element 
            nums1[idxs[i]+i] = nums2[i]
        return
    
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """ 
        if n == 0:
            return
        
        idxs = self.bisect_find(nums1, m, nums2, n)
        
        self.insert(nums1, m, nums2, n, idxs)
        
        return
