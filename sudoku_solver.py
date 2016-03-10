import numpy as np
fname = "sudoku-task1.txt"
#fname = "sudoku-task2.txt"
with open(fname) as f:
    array=[]
    for line in f:
        for symbol in line:
            if (symbol!=" ")&(symbol!="\n"):
                array.append(symbol)
sudoku=[]
for char in array:
    sudoku.append(int(char))
field = np.asarray(sudoku)
field = np.reshape(field,(9,9))
print("Sudoku to solve")
print(field)


def isInArray(array, char):
    if char in array:
        return True
    else:
        return False

def isSolved(array,0)
    if 0 in array:
        return False
    else:
        return True

def get_cell(array, row, column)
    row_index=row/3+1
    column_index=row/3+1
    return array[3*row_index-1:3*row_index+2,3*column_index-1:3*column_index+2]

def checkRow(array, row)
    if isInArray
def checkColumn(array, column)

while not isSolved(field,0)
    for column in range(9):
        for row in range(9):
                if not (field[row,column] == 0):
                    continue
                
    

