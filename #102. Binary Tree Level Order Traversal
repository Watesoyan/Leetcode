class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        nextroots = [root]  
        result = [[root.val]]
        
        while True:
            tmproots = nextroots
            nextroots = []
            tmpvals = []
            
            for tmproot in tmproots:
            
                if tmproot.left is not None:
                    tmpvals.append(tmproot.left.val)
                    nextroots.append(tmproot.left)
            
                if tmproot.right is not None:
                    tmpvals.append(tmproot.right.val)
                    nextroots.append(tmproot.right)
            
            if len(tmpvals) is 0:
                return result
            else:
                result.append(tmpvals)
