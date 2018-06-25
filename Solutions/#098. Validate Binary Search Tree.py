# recurrence version

class Solution(object):
    def ValidBST(self, root):
        
        """
        min <- min(left_min, right_min, root)
        max <- max(left_max, right_max, root)
        """
        
        if root is None:
            return [True, None, None]
        
        rootval = root.val
        
        result = [True, rootval, rootval]
        
        if root.left is None and root.right is None:
            return result
        
        if root.left is not None:
            [leftisvalid, left_max, left_min] = self.ValidBST(root.left)
            
            if not(leftisvalid) or not(rootval > left_max):
                result[0] = False
                return result
            result[1] = max(left_max, result[1])
            result[2] = min(left_min, result[2])
            
        if root.right is not None:
            [rightisvalid, right_max, right_min] = self.ValidBST(root.right)
            
            if not(rightisvalid) or not(rootval < right_min):
                result[0] = False
                return result
            result[1] = max(right_max, result[1])
            result[2] = min(right_min, result[2])
        
        return result
    
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.ValidBST(root)[0]
