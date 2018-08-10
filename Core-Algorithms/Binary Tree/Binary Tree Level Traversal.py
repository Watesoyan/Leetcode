"""
Level Traversal
"""

def LevelTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    if root is None:
        return res
    this_stack = [root]
    next_stack = []
    while len(this_stack) > 0:
        n = len(this_stack)
        level_res = [0] * n
        for i in range(n):
            tmp_root = this_stack[i]
            level_res[i] = tmp_root.val
            if tmp_root.left is not None:
                next_stack.append(tmp_root.left)
            if tmp_root.right is not None:
                next_stack.append(tmp_root.right)

        res.append(level_res)
        this_stack = next_stack
        next_stack = []
    return res
