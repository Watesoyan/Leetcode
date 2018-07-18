class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        L1 = len(haystack)
        L2 = len(needle)
        
        for start in range(L1 - L2 + 1):
            if haystack[start : start+L2] == needle:
                return start
        else:
            return -1
