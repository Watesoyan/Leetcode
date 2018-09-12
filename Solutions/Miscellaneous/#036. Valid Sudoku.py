class Solution(object):
    # note that LeetCode don't support `copy` on `list`, but on `set` and `dict`
    
    # use `nested list` to keep record, faster
    def isValidSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        row_bin    = [[False for i in range(9)] for j in range(9)]    # row_bin[i][j-1] indicates that j has been found in row i
        column_bin = [[False for i in range(9)] for j in range(9)]    # column_bin[i][j-1] indicates that j has been found in column i
        grid_bin   = [[False for i in range(9)] for j in range(9)]    # grid_bin[i][j-1] indicates that j has been found in grid i
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] != ".":
                    
                    n = int(board[i][j]) - 1
                    
                    if row_bin[i][n] :
                        return False
                    
                    if column_bin[j][n]:
                        return False
                    
                    grid_idx = 3*(i//3) + j//3
                    
                    if grid_bin[grid_idx][n]:
                        return False
                        
                    row_bin[i][n]         = True
                    column_bin[j][n]      = True
                    grid_bin[grid_idx][n] = True
                               
        return True
    
    # use `dict` to keep record, slower
    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        bool_array = {(i,j):False for i in range(9) for j in range(9)}
        row_bin    = bool_array.copy()    # row_bin[i][j-1] indicates that j has been found in row i
        column_bin = bool_array.copy()    # column_bin[i][j-1] indicates that j has been found in column i
        grid_bin   = bool_array.copy()    # grid_bin[i][j-1] indicates that j has been found in grid i
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] != ".":
                    
                    n = int(board[i][j]) - 1
                    
                    if row_bin[(i, n)]:
                        return False
                    
                    if column_bin[(j, n)]:
                        return False
                    
                    grid_idx = 3*(i//3) + j//3
                    
                    if grid_bin[(grid_idx, n)]:
                        return False
                        
                    row_bin[(i, n)]         = True
                    column_bin[(j, n)]      = True
                    grid_bin[(grid_idx, n)] = True
                               
        return True
