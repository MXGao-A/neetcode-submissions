class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check each line:
        for i in range(9):
            freq={}
            for num in board[i]:
                if num not in freq:
                    freq[num]=1
                elif num in freq and num!=".":
                    return False
        #check each column:
        for j in range(9):
            freq={}
            for i in range(9):
                if board[i][j] in freq and board[i][j]!=".":
                    return False
                elif board[i][j] not in freq:
                    freq[board[i][j]]=1
        submatrix_start=[(0,0),[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        for x,y in submatrix_start:
            freq={}
            for i in range(0,3):
                for j in range(0,3):
                    if board[x+i][y+j] in freq and board[x+i][y+j]!=".":
                        return False
                    elif board[x+i][y+j] not in freq:
                        freq[board[x+i][y+j]]=1

        return True