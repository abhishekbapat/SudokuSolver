def validate_puzzle(arr):
    if len(arr) != 9:
        return False
    for i in range(9):
        if len(arr[i]) != 9:
            return False
    return True


def print_sudoku(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print('\n')


def find_next_void(arr, loc):
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                loc[0] = i
                loc[1] = j
                return True
    return False


def element_exists_in_row(arr, row, elem):
    for i in range(9):
        if arr[row][i] == elem:
            return True
    return False


def element_exists_in_col(arr, col, elem):
    for i in range(9):
        if arr[i][col] == elem:
            return True
    return False


def element_exists_in_box(arr, row, col, elem):
    r = row - row % 3
    c = col - col % 3
    for i in range(3):
        for j in range(3):
            if arr[r + i][c + j] == elem:
                return True
    return False


def is_safe(arr, row, col, elem):
    return (not element_exists_in_row(arr, row, elem)) and \
            (not element_exists_in_col(arr, col, elem)) and \
            (not element_exists_in_box(arr, row, col, elem))


def solve_sudoku(arr):
    loc = [0, 0]
    if not find_next_void(arr, loc):
        return True

    row = loc[0]
    col = loc[1]

    for num in range(1, 10):
        if is_safe(arr, row, col, num):
            arr[row][col] = num
            if solve_sudoku(arr):
                return True
            arr[row][col] = 0
    return False
