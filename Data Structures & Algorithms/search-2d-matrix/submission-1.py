class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row=0
        start=0
        end=len(matrix)-1

        while start <= end:
            mid= (start+end)//2
            x=matrix[mid][0]
            if target == x:
                return True
            if target < x:
                if mid == 0:
                    return False
                y=matrix[mid-1][0]

                if y <= target < x:
                    row=mid-1
                    break
                
                end=mid-1
            else:
                if mid==end:
                    row=end
                    break
                y=matrix[mid+1][0]
                if x < target < y:
                    row=mid
                    break
                start = mid+1
        
        start = 0
        end=len(matrix[0]) - 1

        while start <= end:
            mid=(start+end)//2

            x=matrix[row][mid]
            if target == x:
                return True
            elif target < x:
                end=mid-1
            else:
                start=mid+1
        return False

        