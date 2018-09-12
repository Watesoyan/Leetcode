class Solution:
    # with recurrence
    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        if root is None:
            return result
        
        result += self.postorderTraversal(root.left)
        result += self.postorderTraversal(root.right)
        result.append(root.val)
        
        return result
    
    # without recurrence
    def postorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        
        p = root
        
        stack = []
        visitedNode = None
        
        while True:
            # visit left child
            while p is not None:
                stack.append(p)
                p = p.left
            
            if len(stack) > 0:
                p = stack[-1]
            else:
                return result
            
            # whether right child exists or is visited or not
            if p.right is not None and p.right is not visitedNode: 
                p = p.right
            else:
                stack.pop()
                result.append(p.val) 
                visitedNode = p
                p = None  # reinitialize p
