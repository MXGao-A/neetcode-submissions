class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        first_col=None
        for i in range(m):
            if matrix[i][0]==0:
                first_col=0
                break
        first_row=None
        for j in range(n):
            if matrix[0][j]==0:
                first_row=0
                break
        for j in range(1,n):
            for i in range(1,m):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    break
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    break
        for j in range(1,n):
            if matrix[0][j]==0:
                for i in range(m):
                    matrix[i][j]=0
        for i in range(1,m):
            if matrix[i][0]==0:
                for j in range(n):
                    matrix[i][j]=0
        if first_col==0:
            for i in range(m):
                matrix[i][0]=0
        if first_row==0:
            for j in range(n):
                matrix[0][j]=0