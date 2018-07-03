class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        max_area = 0
        
        for i0 in range(m):
            n = len(grid[i0])
            i = i0
            for j0 in range(n):
                j = j0
                if grid[i][j] == 0:
                    continue
                
                tmp_area = 1
                grid[i][j] = 0
                stack = []
                
                while True:
                    
                    if i != 0 and grid[i-1][j] == 1:
                        stack.append((i,j))
                        i -= 1
                    elif i != m-1 and grid[i+1][j] == 1:
                        stack.append((i,j))
                        i += 1
                    elif j != 0 and grid[i][j-1] == 1:
                        stack.append((i,j))
                        j -= 1
                    elif j != n-1 and grid[i][j+1] == 1:
                        stack.append((i,j))
                        j += 1
                    elif len(stack) > 0:
                        (i, j) = stack.pop()
                        continue
                    else:
                        break
                    grid[i][j] = 0
                    tmp_area += 1
                
                if tmp_area > max_area:
                    max_area = tmp_area
                
        return max_area
