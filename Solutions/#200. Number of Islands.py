class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        
        if not m :
            return 0
            
        n = len(grid[0])
        island_num = m * n
        
        dirs = ((1,0), (0,1))
        pre = {(i,j):(i,j) for i in range(m) for j in range(n)}
        
        isvalid = lambda i,j: 0 <= i < m and 0 <= j < n
        
        for i in range(m):
            for j in range(n):
                
                ij = (i, j)
                
                if grid[i][j] == "0":
                        island_num -= 1
                    
                else:
                        
                    for dir in dirs:
                        ij_tmp = i_tmp, j_tmp = i+dir[0], j+dir[1]

                        if isvalid(i_tmp, j_tmp) and grid[i_tmp][j_tmp] == "1":

                            # find root of (i,j), using path splitting 
                            ij_rank = 0
                            ij_pre = ij
                            while pre[ij_pre] is not ij_pre:
                                ij_pre = pre[pre[ij_pre]]
                                ij_rank += 1
                            ij_root = ij_pre

                            # find root of (i_tmp,j_tmp), using path splitting 
                            ij_tmp_rank = 0
                            ij_tmp_pre = ij_tmp
                            while pre[ij_tmp_pre] is not ij_tmp_pre:
                                ij_tmp_pre = pre[pre[ij_tmp_pre]]
                                ij_tmp_rank += 1
                            ij_tmp_root = ij_tmp_pre
                            
                            # merge 
                            if ij_root != ij_tmp_root:
                                island_num -= 1
                                if ij_rank < ij_tmp_rank:
                                    pre[ij_root] = ij_tmp_root
                                else:
                                    pre[ij_tmp_root] = ij_root
        
        return island_num
