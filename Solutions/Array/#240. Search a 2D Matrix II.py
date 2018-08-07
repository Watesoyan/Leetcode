class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        
        if n > 0:
            i, j = 0, len(matrix[0])-1
            while j > -1 and i < len(matrix):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:
                    i += 1
                else:
                    j -= 1
        return False
