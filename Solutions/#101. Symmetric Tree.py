class Solution:
    def isMirrorTree(self, p, q):
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
        
        return p.val == q.val and self.isMirrorTree(p.left, q.right) and self.isMirrorTree(p.right, q.left)
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        
        return self.isMirrorTree(root.left, root.right)
