def is_valid_sudoku(board):
    def is_valid_unit(unit):
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))
    
    for row in board:
        if not is_valid_unit(row):
            return False
    
    for col in zip(*board):
        if not is_valid_unit(col):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            unit = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(unit):
                return False
    return True
