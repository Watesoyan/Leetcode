class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        bool1 = p is None
        bool2 = q is None
        
        if bool1 and bool2:
            return True
        elif bool1 or bool2:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
