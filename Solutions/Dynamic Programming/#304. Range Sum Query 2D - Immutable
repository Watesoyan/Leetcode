class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        
        m = len(matrix)
        n = len(matrix[0])
        self.cumsum = [[0 for j in range(n+1)] for i in range(m+1)]
        # cumsum along columns
        for i in range(m):
            for j in range(n):
                self.cumsum[i+1][j+1] = self.cumsum[i+1][j] + matrix[i][j]
        # cumsum along rows
        for i in range(m):
            for j in range(n):
                self.cumsum[i+1][j+1] += self.cumsum[i][j+1]
        return

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.cumsum[row2+1][col2+1] + self.cumsum[row1][col1] - self.cumsum[row2+1][col1] - self.cumsum[row1][col2+1]
