class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #horizontal
        for arr in board:
            numbers_only = [x for x in arr if x.isdigit()]
            if len(numbers_only) != len(set(numbers_only)):
                return False
        #vertical:
        #turn it in horizontal
        for index in range(9):
            temp = []
            for arr in board:
                temp.append(arr[index])
            numbers_only = [x for x in temp if x.isdigit()]
            if len(numbers_only) != len(set(numbers_only)):
                return False
        #box
        #4 loop 
        for box_start_row in range(0,9,3):
            for box_start_col in range(0,9,3):
                temp = []
                for current_row in range(box_start_row, box_start_row+3):
                    for current_col in range(box_start_col, box_start_col+3):
                        temp.append(board[current_col][current_row])
                numbers_only = [x for x in temp if x.isdigit()]
                if len(numbers_only) != len(set(numbers_only)):
                    return False   

        return True 