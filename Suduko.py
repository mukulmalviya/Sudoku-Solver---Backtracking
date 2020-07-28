#!/usr/bin/python3

sudoku = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#points -rules -findempty -display -backtrackAlgorithm

#display sudoku

def display_sudoku(sudoku):
    for i in range(len(sudoku)):
        if i%3 == 0 and i != 0:
            print("-------------------------")
        for j in range(len(sudoku[0])):
            if j%3 == 0 and j != 0:
                print("|", end=" ")
            print(str(sudoku[i][j]) ,end=" ")
        print()

def find_empty(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku[0])):
            if sudoku[i][j] == 0:
                return (i,j) #row and column

def rules(sudoku,item,position):
    #horizontal condition
    for i in range(len(sudoku[0])):
        if item == sudoku[position[0]][i] and position[1] != i:
            return False

    #vertical condition
    for i in range(len(sudoku)):
        if item == sudoku[i][position[1]] and position[0] != i:
            return False

    #3x3 condition
    box_x = position[0] // 3
    box_y = position[1] // 3

    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if sudoku[i][j] == item and position != (i,j):
                return False
    return True

#algoritmn here
def solve(sudoku):
    find = find_empty(sudoku)
    if not find:
        return True
    else:
        (row,col) = find
    for i in range(1,11):
        if rules(sudoku,i,(row,col)):
            sudoku[row][col] = i
            if solve(sudoku):
                return True
            sudoku[row][col] = 0
    return  False

display_sudoku(sudoku) #before
solve(sudoku)
print("++++++++++++++++++++++++++++++")
print("++++++++++++++++++++++++++++++")
display_sudoku(sudoku) #after
