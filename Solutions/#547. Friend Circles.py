class Solution:
    # based on union-find set 
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n = len(M)
        circle_num = n
        pre = {i:i for i in range(n)}
        
        for i in range(n):
            for j in range(i,n):
                if M[i][j] :
                    
                    # find root of i, using path splitting 
                    i_rank = 0
                    i_pre = i
                    while pre[i_pre] is not i_pre:
                        i_pre = pre[pre[i_pre]]
                        i_rank += 1
                    i_root = i_pre
                    
                    # find root of j, using path splitting
                    j_rank = 0
                    j_pre = j
                    while pre[j_pre] is not j_pre:
                        j_pre = pre[pre[j_pre]]
                        j_rank += 1
                    j_root = j_pre
                    
                    # merge 
                    if i_root != j_root:
                        circle_num -= 1
                        if i_rank < j_rank:
                            pre[i_root] = j_root
                        else:
                            pre[j_root] = i_root
        
        return circle_num
