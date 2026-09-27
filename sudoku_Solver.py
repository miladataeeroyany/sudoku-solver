sudoku = [[0]*9 for _ in range(9)]

def inputSudoku():
    print("Choose one of the following methods to enter Sudoku numbers.")
    print("1- Enter each row as a single 9-digit line (use 0 for empty cells).")
    print("2- Enter numbers with address (e.g., 123 = row 1, col 2, value 3).")
    
    try:
        typeInput = int(input(">>> "))
    except ValueError:
        print("Invalid input.")
        return False
    
    if typeInput == 1:
        for i in range(9):
            while True:
                line = input(f"Line {i+1}: ").strip()
                if len(line) == 9 and line.isdigit():
                    for j in range(9):
                        sudoku[i][j] = int(line[j])
                    break
                else:
                    print("The input must consist of 9 digits. Please again...")
                    
    elif typeInput == 2:
        while True:
            iputValue = input(">>> ").strip()
            if iputValue.lower() == "end":
                break
            if len(iputValue) == 3 and iputValue.isdigit():
                r, c, v = int(iputValue[0]), int(iputValue[1]), int(iputValue[2])
                if 1 <= r <= 9 and 1 <= c <= 9 and 1 <= v <= 9:
                    sudoku[r-1][c-1] = v
                else:
                    print("Invalid range. Use 1-9 for row, column, and value.")
            else:
                print("Invalid input. Please enter exactly 3 digits.")
    else:
        print("Invalid choice.")
        return False
    
    return True

def isValid(row, col, num):
    for i in range(9):
        if sudoku[i][col] == num or sudoku[row][i] == num:
            return False
    xStart, yStart = (row//3)*3, (col//3)*3
    for i in range(xStart, xStart+3):
        for j in range(yStart, yStart+3):
            if sudoku[i][j] == num:
                return False
    return True

def solved():
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                for k in range(1, 10):
                    if isValid(i, j, k):
                        sudoku[i][j] = k
                        if solved():
                            return True
                        sudoku[i][j] = 0
                return False
    return True

if __name__ == "__main__":
    if inputSudoku():
        if solved():
            for row in sudoku:
                print(row)
        else:
            print("I can't solve it")