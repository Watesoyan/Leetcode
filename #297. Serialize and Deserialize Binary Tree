class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return []
        
        nextroots = [root]  
        result = [root.val]
        
        while True:
            tmproots = nextroots
            nextroots = []
            tmpvals = []
            
            for tmproot in tmproots:
            
                if tmproot.left is None:
                    tmpvals.append(None)
                else:
                    tmpvals.append(tmproot.left.val)
                    nextroots.append(tmproot.left)
            
                if tmproot.right is None:
                    tmpvals.append(None)
                else:
                    tmpvals.append(tmproot.right.val)
                    nextroots.append(tmproot.right)
            
            if len(tmpvals) is 0:
                return result
            else:
                result += tmpvals

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) is 0:
            return None
        
        n = len(data)
        
        nodes = [None if x is None else TreeNode(x) for x in data]
                
        parentIdx = 0
        childIdx = 1
        
        while childIdx < n:
            parentnode = nodes[parentIdx]
            if parentnode is None:
                parentIdx += 1
            else:
                parentnode.left = nodes[childIdx]
                if childIdx + 1 == n:
                    return nodes[0]
                parentnode.right = nodes[childIdx + 1]
                parentIdx += 1
                childIdx += 2
        
        return nodes[0]
