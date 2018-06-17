class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        elif root.left is None and root.right is None:
            return 1
        
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
