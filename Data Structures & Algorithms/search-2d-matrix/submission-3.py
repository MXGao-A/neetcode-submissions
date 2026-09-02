class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #first search for the row
        up,down=0,len(matrix)-1
        within_row=False
        while up<=down:
            mid=(up+down)//2
            if target>matrix[mid][-1]:
                up=mid+1
            elif target<matrix[mid][0]:
                down=mid-1
            elif target==matrix[mid][-1] or target==matrix[mid][0]:
                return True
            else:
                final_row=mid
                within_row=True
                break
        #now the search constraints to the up/down th row.
        if not within_row:
            return False
        left,right=0,len(matrix[final_row])-1
        while left<=right:
            mid=(left+right)//2
            if target>matrix[final_row][mid]:
                left=mid+1
            elif target<matrix[final_row][mid]:
                right=mid-1
            else:
                return True
        return False
