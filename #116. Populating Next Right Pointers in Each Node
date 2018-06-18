class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        
        root.next = None
        nextroots = [root]  
        
        while len(nextroots) > 0:
            tmproots = nextroots
            next0 = None
            nextroots = []
            
            for tmproot in tmproots:
                
                tmpright = tmproot.right
                tmpleft = tmproot.left
                
                if tmpright is not None:
                    tmpright.next = next0
                    next0 = tmpright
                    nextroots.append(tmpright)
            
                if tmpleft is not None:
                    tmpleft.next = next0
                    next0 = tmpleft
                    nextroots.append(tmpleft)
