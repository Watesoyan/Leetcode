def DFS(self, matrix, i, j, old_marker, new_marker, ignore_boundary=False):
	
	if old_marker == new_marker:       # handle the special case
		return matrix
	
	m = len(matrix)
	n = len(matrix[0])
	
	matrix[i][j] = new_marker
	stack = []
	
	if ignore_boundary:
		while True:
			if matrix[i-1][j] == old_marker:
				stack.append((i,j))
				i -= 1           
			elif matrix[i+1][j] == old_marker:
				stack.append((i,j))
				i += 1
			elif matrix[i][j-1] == old_marker:
				stack.append((i,j))
				j -= 1
			elif matrix[i][j+1] == old_marker:
				stack.append((i,j))
				j += 1
			elif len(stack) > 0:
				(i, j) = stack.pop()
				continue
			else:
				break
			matrix[i][j] = new_marker
	else:
		while True:
			if i != 0 and matrix[i-1][j] == old_marker:
				stack.append((i,j))
				i -= 1
			elif i != m-1 and matrix[i+1][j] == old_marker:
				stack.append((i,j))
				i += 1
			elif j != 0 and matrix[i][j-1] == old_marker:
				stack.append((i,j))
				j -= 1
			elif j != n-1 and matrix[i][j+1] == old_marker:
				stack.append((i,j))
				j += 1
			elif len(stack) > 0:
				(i, j) = stack.pop()
				continue
			else:
				break
			matrix[i][j] = new_marker
	return