import lib.sudoku_solver as solver

Arr = [[3, 0, 0, 0, 0, 9, 8, 0, 1],
       [0, 0, 6, 0, 0, 0, 0, 0, 9],
       [8, 0, 0, 0, 7, 0, 0, 0, 0],
       [0, 0, 0, 4, 0, 0, 0, 0, 0],
       [5, 0, 0, 0, 0, 0, 0, 6, 0],
       [0, 7, 0, 0, 8, 0, 1, 3, 0],
       [0, 1, 0, 0, 0, 0, 4, 0, 0],
       [0, 0, 0, 2, 0, 3, 9, 0, 0],
       [0, 5, 4, 0, 0, 1, 0, 0, 0]]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if solver.solve_sudoku(Arr):
        solver.print_sudoku(Arr)
    else:
        print("Solution the above problem does not exist")
