class Solution(object):
    def treeHeight(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return 0
        else:
            return 1 + max(self.treeHeight(root.left), self.treeHeight(root.right))
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return abs(self.treeHeight(root.left) - self.treeHeight(root.right)) <= 1 \
                and self.isBalanced(root.left) and self.isBalanced(root.right)
