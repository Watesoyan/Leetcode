class Solution(object):
    # apply post-order search in finding lowest common ancestor
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        ptr = root
        stack = [] # stack contains ancester of found first node, p or q
        idx = -1  # index of ancestor
        pfound = False
        qfound = False
        
        visitedNode = None
        
        flag = 0 # whether or not p and q in same sub-tree
        
        while True:
            # visit left child
            while ptr is not None:
                stack.append(ptr)
                ptr = ptr.left
                if not(pfound or qfound):
                    idx += 1
            
            if len(stack) > 0:
                ptr = stack[-1]
            else:
                return None
            
            # whether right child exists or is visited or not
            if ptr.right is not None and ptr.right is not visitedNode:
                if pfound or qfound:
                    flag = 1
                ptr = ptr.right
            else:
                stack.pop()
                
                if len(stack) < idx + 1:
                    idx -= 1
                    if pfound or qfound:
                        flag = 0
                
                if ptr.val == p.val:
                    pfound = True
                if ptr.val == q.val:
                    qfound = True
                
                if pfound and qfound:
                    # flag == 1 when p and q are in the different sub-tree
                    if len(stack) > idx + 1 or flag == 1: 
                        return stack[idx]
                    else:
                        return ptr
                
                visitedNode = ptr
                ptr = None  # reinitialize ptr
