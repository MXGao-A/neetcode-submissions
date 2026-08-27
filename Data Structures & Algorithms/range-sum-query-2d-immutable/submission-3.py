class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m=len(matrix)
        n=len(matrix[0])
        self.p=[[0] *n  for j in range(m)]
        for i in range(m):
            for j in range(n):
                if (i-1)<0 and (j-1)>=0:
                    self.p[i][j]=matrix[i][j]+0+self.p[i][j-1]-0
                elif (j-1)<0 and (i-1)>=0:
                    self.p[i][j]=matrix[i][j]+self.p[i-1][j]+0-0
                elif (j-1)<0 and (i-1)<0:
                    self.p[i][j]=matrix[i][j]
                else:
                    self.p[i][j]=matrix[i][j]+self.p[i-1][j]+self.p[i][j-1]-self.p[i-1][j-1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        first=self.p[row2][col2]

        if (row1-1)<0 and (col1-1)>=0:
            second=0
            fourth=0
            third=self.p[row2][col1-1]
        elif (col1-1)<0 and (row1-1)>=0:
            third=0
            fourth=0
            second=self.p[row1-1][col2]
        elif (col1-1)>=0 and (row1-1)>=0:
            second=self.p[row1-1][col2]
            third=self.p[row2][col1-1]
            fourth=self.p[row1-1][col1-1]
        elif (col1-1)<0 and (row1-1)<0:
            second=0
            third=0
            fourth=0
        return first-second-third+fourth

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)