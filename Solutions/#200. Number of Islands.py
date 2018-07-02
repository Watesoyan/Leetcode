class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        num_Islands = 0
        
        for i0 in range(m):
            n = len(grid[i0])
            i = i0
            for j0 in range(n):
                j = j0
                if grid[i][j] == '0':
                    continue
                
                grid[i][j] = '0'
                stack = []
                
                while True:
                    if i != 0 and grid[i-1][j] == '1':
                        stack.append((i,j))
                        i -= 1
                        grid[i][j] = '0'
                    elif i != m-1 and grid[i+1][j] == '1':
                        stack.append((i,j))
                        i += 1
                        grid[i][j] = '0'
                    elif j != 0 and grid[i][j-1] == '1':
                        stack.append((i,j))
                        j -= 1
                        grid[i][j] = '0'
                    elif j != n-1 and grid[i][j+1] == '1':
                        stack.append((i,j))
                        j += 1
                        grid[i][j] = '0'
                    elif len(stack) > 0:
                        (i, j) = stack.pop()
                    else:
                        break
                num_Islands += 1
                
        return num_Islands
