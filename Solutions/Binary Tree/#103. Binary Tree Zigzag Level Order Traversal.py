class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        layeridx = 1
        result = []
        nextroots = [root]
        tmpvals = []
        
        while len(nextroots) != 0:
            if layeridx % 2 == 1:
                nextroots.reverse()
                tmproots = nextroots
                nextroots = []
            
                for tmproot in tmproots:
                    tmpvals.append(tmproot.val)
                
                    if tmproot.left is not None:
                        nextroots.append(tmproot.left)
            
                    if tmproot.right is not None:
                        nextroots.append(tmproot.right)
            
            else:
                nextroots.reverse()
                tmproots = nextroots
                nextroots = []
                    
                for tmproot in tmproots:
                    tmpvals.append(tmproot.val)
                    
                    if tmproot.right is not None:
                        nextroots.append(tmproot.right)
            
                    if tmproot.left is not None:
                        nextroots.append(tmproot.left)
            
            result.append(tmpvals)
            tmpvals = []
            layeridx += 1
            
        return result      
