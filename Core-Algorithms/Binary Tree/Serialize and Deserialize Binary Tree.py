class TreeNode:
    def __repr__(self):
        return '[{0}, {1}, {2}]'.format(self.val, self.left, self.right)
        
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        return

class Solution:
    def Serialize(self, root):
        if root is None:
            return []
        this_stack = [root]
        res = []
        
        while len(this_stack) > 0:
            notallNone = False
            next_stack = []
            for tmp_root in this_stack:
                if tmp_root is None:
                    res.append(None)
                else:
                    res.append(tmp_root.val)
                    next_stack.append(tmp_root.left)
                    next_stack.append(tmp_root.right)
                    if tmp_root.left is not None or tmp_root.right is not None:
                        notallNone = True
            this_stack = next_stack
            if not notallNone:
                break
        return res
        
    def Deserialize(self, s):
        n = len(s)
        if n == 0:
            return None
        makeTreeNode = lambda x: None if x is None else TreeNode(x)
        nodes = list(map(makeTreeNode, s))
        i, j = 0, 1
        while i < j < n:
            p = nodes[i]
            if p is not None:
                p.left = nodes[j]
                j += 1
                p.right = nodes[j]
                j += 1
            i += 1
        return nodes[0]
