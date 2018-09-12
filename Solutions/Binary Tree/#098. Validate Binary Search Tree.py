class Solution(object):    
    # non-recurrence version
    def isValidBST2(self, root):
        pre = None
        stack = []
        p = root

        while True:
            while p is not None:
                stack.append(p)
                p = p.left

            if len(stack) > 0:
                p = stack.pop()
                if pre is None or pre < p.val:
                    pre = p.val
                else:
                    return False
            else:
                return True

            if p.right is None:
                p = None        # reinitialize p
            else:
                p = p.right
