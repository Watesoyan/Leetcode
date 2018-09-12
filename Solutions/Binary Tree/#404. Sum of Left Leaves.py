class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        if root.left is None:
            left =  0
        elif root.left.left is None and root.left.right is None:
            left = root.left.val
        else:
            left = self.sumOfLeftLeaves(root.left)
        
        if root.right is None:
            right =  0
        else:
            right = self.sumOfLeftLeaves(root.right)
        
        return left + right
