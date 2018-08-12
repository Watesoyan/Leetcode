# build tree according to its preorder and inorder
def buildTree(self, preorder, inorder):
	"""
	:type preorder: List[int]
	:type inorder: List[int]
	:rtype: TreeNode
	"""
	"""
	preorder: [root left right]
	inorder:  [left root right]
	""" 
	
	if len(preorder) == 0:
		return None
	
	L = len(preorder)
	
	pre_idx_stack = [(0, L)]
	offset_stack = [0]
	
	hash_inorder = {inorder[i]:i for i in range(L)}
	
	nodes = list(map(TreeNode, preorder))
	
	while len(pre_idx_stack) > 0:
		
		pre_min, pre_max = pre_idx_stack.pop()
		
		offset = offset_stack.pop()
		
		tmp_root = nodes[pre_min]
		
		tmp_left = tmp_right = None
		
		if pre_max - pre_min != 1: 
			
			root_idx = hash_inorder[preorder[pre_min]] - offset
				 
			if root_idx != pre_min :
				tmp_left = nodes[pre_min + 1]
				if root_idx != pre_min + 1:   
					pre_idx_stack.append((pre_min + 1, root_idx + 1))
					offset_stack.append(offset - 1)
				
			if root_idx != pre_max - 1:
				tmp_right = nodes[root_idx + 1]
				if root_idx != pre_max - 2:
					pre_idx_stack.append((root_idx + 1, pre_max))
					offset_stack.append(offset)
		
		tmp_root.left = tmp_left
		tmp_root.right = tmp_right
		
	return nodes[0]
