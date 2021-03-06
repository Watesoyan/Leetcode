class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        
        rootval = root.val
        nextsum = sum - rootval
        
        L = root.left is None
        R = root.right is None
        
        if L and R:
            if nextsum == 0:
                return [[rootval]]
            else:
                return []
        
        if L:
            return [[rootval]+path for path in self.pathSum(root.right, nextsum)]
        if R:
            return [[rootval]+path for path in self.pathSum(root.left, nextsum)]
        
        tmplist = self.pathSum(root.left, nextsum) + self.pathSum(root.right, nextsum)
        
        return  [[rootval]+path for path in tmplist]
