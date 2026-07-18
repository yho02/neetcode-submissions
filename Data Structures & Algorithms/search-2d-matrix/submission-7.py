class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, (m*n) - 1
        while l <= r:
            mid = l + (r-l) //2
            p = matrix[mid//n][mid%n]
            print(p)
            if p == target:
                return True
            elif p < target:
                # target in right half
                l = mid + 1
            elif p > target:
                r = mid - 1
        return False 
            
