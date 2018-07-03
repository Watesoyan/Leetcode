class Solution:
    def DFS(self, board, i, j, marker, ignore_boundary=False):
        m = len(board)
        n = len(board[0])
        
        board[i][j] = marker
        stack = []
        
        if ignore_boundary:
            while True:
                if board[i-1][j] == 'O':
                    stack.append((i,j))
                    i -= 1           
                elif board[i+1][j] == 'O':
                    stack.append((i,j))
                    i += 1
                elif board[i][j-1] == 'O':
                    stack.append((i,j))
                    j -= 1
                elif board[i][j+1] == 'O':
                    stack.append((i,j))
                    j += 1
                elif len(stack) > 0:
                    (i, j) = stack.pop()
                    continue
                else:
                    break
                board[i][j] = marker
        else:
            while True:
                if i != 0 and board[i-1][j] == 'O':
                    stack.append((i,j))
                    i -= 1
                elif i != m-1 and board[i+1][j] == 'O':
                    stack.append((i,j))
                    i += 1
                elif j != 0 and board[i][j-1] == 'O':
                    stack.append((i,j))
                    j -= 1
                elif j != n-1 and board[i][j+1] == 'O':
                    stack.append((i,j))
                    j += 1
                elif len(stack) > 0:
                    (i, j) = stack.pop()
                    continue
                else:
                    break
                board[i][j] = marker
        return
                        
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        
        if m == 0:
            return
        
        n = len(board[0])
        
        boundary = [(i, j) for i in (0, m-1) for j in range(n)]+[(i, j) for i in range(1, m-1) for j in (0, n-1)]
        
        for i, j in boundary:
            if board[i][j] == 'O':
                self.DFS(board, i, j, 'B', ignore_boundary=False)
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    self.DFS(board, i, j, 'T', ignore_boundary=True)      
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                elif board[i][j] == 'T':
                    board[i][j] = 'X'
        
        return
