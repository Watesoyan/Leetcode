class Solution:
    def constructBST(self, nums, root):
        n = len(nums)
        if n == 1:
            root.val = nums[0]
        elif n == 2:
            root.val = nums[1]
            root.left = TreeNode(nums[0])
        else:
            mid = n // 2
            root.val = nums[mid]
            pleft = root.left = TreeNode(0)
            pright = root.right = TreeNode(0)
            self.constructBST(nums[:mid], pleft)
            self.constructBST(nums[mid+1:], pright)
        return
        
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        else:
            root = TreeNode(0)
            self.constructBST(nums, root)
            return root
