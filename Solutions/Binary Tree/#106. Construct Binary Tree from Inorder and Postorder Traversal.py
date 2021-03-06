# takes about 52 ms in LeetCode benchmark

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        """
        postorder: [left right root]
        inorder:  [left root right]
        """ 
        
        if len(postorder) == 0:
            return None
        
        L = len(postorder)
        
        post_idx_stack = [(0, L)]
        offset_stack = [0]
        
        hash_inorder = {inorder[i]:i for i in range(L)}
        
        nodes = list(map(TreeNode, postorder))
        
        while len(post_idx_stack) > 0:
            
            post_min, post_max = post_idx_stack.pop()
            
            offset = offset_stack.pop()
            
            tmp_root = nodes[post_max - 1]
            
            tmp_left = None
            tmp_right = None
            
            if post_max - post_min != 1: 
                
                # use most of time
                root_idx = hash_inorder[postorder[post_max-1]] - offset
                   
                if root_idx != post_min :
                    tmp_left = nodes[root_idx - 1]
                    if root_idx != post_min + 1 : 
                        post_idx_stack.append((post_min, root_idx))
                        offset_stack.append(offset)
                    
                if root_idx != post_max - 1 :
                    tmp_right = nodes[post_max - 2]
                    if root_idx != post_max - 2:
                        post_idx_stack.append((root_idx, post_max - 1))
                        offset_stack.append(offset + 1)
            
            tmp_root.left = tmp_left
            tmp_root.right = tmp_right
            
        return nodes[-1]
