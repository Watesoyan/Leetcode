class Solution(object):
    # takes 88 ms in LeetCode Benchmark
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
                    elif i != m-1 and grid[i+1][j] == '1':
                        stack.append((i,j))
                        i += 1
                    elif j != 0 and grid[i][j-1] == '1':
                        stack.append((i,j))
                        j -= 1
                    elif j != n-1 and grid[i][j+1] == '1':
                        stack.append((i,j))
                        j += 1
                    elif len(stack) > 0:
                        (i, j) = stack.pop()
                        continue
                    else:
                        break
                    grid[i][j] = '0'
                
                num_Islands += 1
                
        return num_Islands
