class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = set()
        c = set()
        def rowZero(row):
            for i in range(len(matrix[0])):
                matrix[row][i] = 0
    

        def colZero(col):
            for i in range(len(matrix)):
                matrix[i][col] = 0
                
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
    
        for row in r:
            rowZero(row)
        for col in c:
            colZero(col)
        return matrix

        