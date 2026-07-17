class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        last_index = len(matrix[0]) - 1
        for row in matrix:
            if row[last_index] == target:
                return True
            elif row[last_index] > target:
                for item in row:
                    print(item)
                    if item == target:
                        return True
        return False