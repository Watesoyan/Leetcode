class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        maxWidth = 1
        
        nextidxs = [0]
        nextroots = [root]
        
        while len(nextroots) != 0:
            tmpidxs = nextidxs
            tmproots = nextroots
            nextroots = []
            nextidxs = []
            
            flag = 0 # flag is 1 only when left boundary is found
                   
            for tmpidx,tmproot in zip(tmpidxs, tmproots):
                
                if tmproot.left is not None:
                    idx = 2*tmpidx
                    nextroots.append(tmproot.left)
                    nextidxs.append(idx)
                    if flag == 0:
                        flag = 1
                        left = idx
                    
                    right = idx
                
                if tmproot.right is not None:
                    idx = 2*tmpidx+1
                    nextroots.append(tmproot.right)
                    nextidxs.append(idx)
                    if flag == 0:
                        flag = 1
                        left = idx
                    
                    right = idx

            if flag == 1:
                tmpWidth = right - left + 1
                if tmpWidth > maxWidth:
                    maxWidth = tmpWidth
            
        return maxWidth
