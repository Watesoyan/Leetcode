"""
Pre-order Traversal
"""

# with recurrence
def preorderTraversal1(self, root):
	"""
	:type root: TreeNode
	:rtype: List[int]
	"""
	result = []
	
	if root is None:
		return result
	
	result.append(root.val)
	result += self.preorderTraversal(root.left)
	result += self.preorderTraversal(root.right)
	
	return result
    
# without recurrence
def preorderTraversal2(self, root):
	"""
	:type root: TreeNode
	:rtype: List[int]
	"""
	
	result = []
	stack = []
	p = root
	
	while True:
		while p is not None:
			result.append(p.val)
			stack.append(p)
			p = p.left
		
		if len(stack) > 0:
			p = stack.pop()
		else:
			return result
		
		# remember that p has been visited
		if p.right is None:
			p = None # reinitialize p
		else:
			p = p.right
			
"""
In-order Traversal
"""

# with recurrence
def inorderTraversal1(self, root):
	"""
	:type root: TreeNode
	:rtype: List[int]
	"""
	result = []
	
	if root is None:
		return result
	
	result += self.inorderTraversal(root.left)
	result.append(root.val)
	result += self.inorderTraversal(root.right)
	
	return result

# without recurrence
def inorderTraversal2(self, root):
	"""
	:type root: TreeNode
	:rtype: List[int]
	"""
	result = []
	stack = []
	p = root
	
	while True:
		while p is not None:
			stack.append(p)
			p = p.left
		
		if len(stack) > 0:
			p = stack.pop()
			result.append(p.val)
		else:
			return result
		
		if p.right is None:
			p = None # reinitialize p
		else:
			p = p.right
			
"""
Post-order Traversal
"""

# with recurrence
def postorderTraversal1(self, root):
	"""
	:type root: TreeNode
	:rtype: List[int]
	"""
	result = []
	
	if root is None:
		return result
	
	result += self.postorderTraversal(root.left)
	result += self.postorderTraversal(root.right)
	result.append(root.val)
	
	return result

# without recurrence
def postorderTraversal2(self, root):
	"""
	:type root: TreeNode
	:rtype: List[int]
	"""
	result = []
	
	p = root
	
	stack = []
	visitedNode = None
	
	while True:
		# visit left child
		while p is not None:
			stack.append(p)
			p = p.left
		
		if len(stack) > 0:
			p = stack[-1]
		else:
			return result
		
		# whether right child exists or is visited or not
		if p.right is not None and p.right is not visitedNode: 
			p = p.right
		else:
			stack.pop()
			result.append(p.val) 
			visitedNode = p
			p = None  # reinitialize p
