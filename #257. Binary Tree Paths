class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        
        flag = 0
        if root.left is not None:
            flag = 1
            leftleaf = self.binaryTreePaths(root.left)
            leftpath = [str(root.val)+"->"+leftleaf0 for leftleaf0 in leftleaf]
        else:
            leftpath = []
        
        if root.right is not None:
            flag = 1
            rightleaf = self.binaryTreePaths(root.right)
            rightpath = [str(root.val)+"->"+rightleaf0 for rightleaf0 in rightleaf]
        else:
            rightpath = []
        
        if flag == 1:
            return leftpath + rightpath
        else:
            return [str(root.val)]
