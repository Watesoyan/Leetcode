class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        nextroots = [root]  
        result = [root.val]
        
        while True:
            tmproots = nextroots
            nextroots = []
            maxval = None
            
            for tmproot in tmproots:
            
                if tmproot.left is not None:
                    nextroots.append(tmproot.left)
                    
                    leftval = tmproot.left.val
                    if maxval is None:
                        maxval = leftval
                    else:
                        maxval = max(maxval, leftval)
            
                if tmproot.right is not None:
                    nextroots.append(tmproot.right)
                    rightval = tmproot.right.val
                    if maxval is None:
                        maxval = rightval
                    else:
                        maxval = max(maxval, rightval)
            
            if maxval is None:
                return result
            else:
                result.append(maxval)
