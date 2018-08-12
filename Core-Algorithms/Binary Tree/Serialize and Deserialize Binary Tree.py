class Solution:
    def Serialize(self, root):
        this_stack = [root]
        res = []
        while len(this_stack) > 0:
            next_stack = []
            for tmp_root in this_stack:
                if tmp_root is None:
                    res.append(None)
                else:
                    res.append(tmp_root.val)
                    next_stack.append(tmp_root.left)
                    next_stack.append(tmp_root.right)   
            this_stack = next_stack
        return res
        
    def Deserialize(self, s):
        n = len(s)
        if n == 0:
            return None
        nodes = [None if x is None else TreeNode(x) for x in s]
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
