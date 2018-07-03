class Solution:
    def DFS(self, board, i, j, old_marker, new_marker, ignore_boundary=False):
        m = len(board)
        n = len(board[0])

        board[i][j] = new_marker
        stack = []
        
        while True:
            if i != 0 and board[i-1][j] == old_marker:
                stack.append((i,j))
                i -= 1
            elif i != m-1 and board[i+1][j] == old_marker:
                stack.append((i,j))
                i += 1
            elif j != 0 and board[i][j-1] == old_marker:
                stack.append((i,j))
                j -= 1
            elif j != n-1 and board[i][j+1] == old_marker:
                stack.append((i,j))
                j += 1
            elif len(stack) > 0:
                (i, j) = stack.pop()
                continue
            else:
                break
            board[i][j] = new_marker
        return

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        
        if oldColor == newColor:
            return image
        
        m = len(image)
        n = len(image[0])
        
        self.DFS(image, sr, sc, oldColor, newColor)
                
        return image
