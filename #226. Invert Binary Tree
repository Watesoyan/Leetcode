class Solution:
    # with recurrence
    def invertTree1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        
        t = TreeNode(root.val)
        t.left = self.invertTree(root.right)
        t.right = self.invertTree(root.left)
        
        return t
    
    # without recurrence, faster
    def invertTree2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        
        nextroots = [root]
        
        while len(nextroots) != 0:
            tmproots = nextroots
            nextroots = []
        
            for tmproot in tmproots:
                           
                if tmproot.left is not None: 
                    nextroots.append(tmproot.left)
                    
                if tmproot.right is not None:
                    nextroots.append(tmproot.right)
                    
                tmp = tmproot.left
                tmproot.left = tmproot.right
                tmproot.right = tmp
                               
        return root
