class Solution:
    # with recurrence
    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        if root is None:
            return result
        
        result.append(root.val)
        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)
        
        return result
    
    # without recurrence
    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        result = []
        stack = []
        p = root
        
        while True:
            while p is not None:
                result.append(p.val)
                stack.append(p)
                p = p.left
            
            if len(stack) > 0:
                p = stack.pop()
            else:
                return result
            
            # remember that p has been visited
            if p.right is None:
                p = None # reinitialize p
            else:
                p = p.right
