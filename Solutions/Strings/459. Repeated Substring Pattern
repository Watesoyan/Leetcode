class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        mid = n >> 1
        for Ls in range(1, mid+1):
            if n % Ls == 0:                             # length of `sub_str` should be a divisor of length of `s`
                sub_str = s[ : Ls]
                start = Ls
                for start in range(Ls, n, Ls):
                    if s[start : start+Ls] != sub_str:  # break loop while `sub_str` not repeated
                        break
                else:
                    return True
        else:
            return False
