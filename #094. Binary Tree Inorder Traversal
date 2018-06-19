class Solution:
    # with recurrence
    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        if root is None:
            return result
        
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        
        return result
    
    # without recurrence
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        p = root
        
        while True:
            while p is not None:
                stack.append(p)
                p = p.left
            
            if len(stack) > 0:
                p = stack.pop()
                result.append(p.val)
            else:
                return result
            
            if p.right is None:
                p = None # reinitialize p
            else:
                p = p.right
