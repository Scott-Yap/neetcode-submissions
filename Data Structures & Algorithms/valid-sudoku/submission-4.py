class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check row 
        for row in board:
            current_row = [x for x in row if x != "."]
            if len(current_row) != len(set(current_row)):
                return False

        # check column
        for col in range(len(board)):
            current_column = [x[col] for x in board]
            current_column = [x for x in current_column if x != "."]
            if len(current_column) != len(set(current_column)):
                return False

        # check box
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                current_box = []
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        current_box.append(board[r][c])
                
                current_box = [x for x in current_box if x != "."]
    
                
                if len(current_box) != len(set(current_box)):
                    return False
        
        return True
    


        
