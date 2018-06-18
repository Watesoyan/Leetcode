class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        
        d = sum - root.val
        
        if root.left is None and root.right is None:
            return d == 0
        
        else:
            return self.hasPathSum(root.left, d) or self.hasPathSum(root.right, d)
