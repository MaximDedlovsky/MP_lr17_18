def sumMatrix(matrix1: list, matrix2: list) -> list:
    result = []
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j], matrix2[i][j])
        result.append(row)
    return result


def mulMatrix(matrix1: list, matrix2: list) -> list:
    if len(matrix1[0]) != len(matrix2):
        return False
    sum = 0
    rowList = []
    result = []
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                sum += matrix1[i][k] * matrix2[k][j]
            rowList.append(sum)
            sum = 0
        result.append(rowList)
        rowList = []
    return result


def GetMatrix(rows: int, cols: int) -> list:
    matrix = []
    for i in range(rows):
        rowList = []
        for j in range(cols):
            rowList.append(random.randint(0, 9))
        matrix.append(rowList)
    return matrix


def PrintMatrix(matrix: list):
    for row in matrix:
        for item in row:
            print(item, end=' ')
        print()

        
rows = int(input('Rows: '))
cols = int(input('Columns: '))
print("Matrix 1: ")
matrix1 = GetMatrix(rows, cols)
PrintMatrix(matrix1)
print("Matrix 2: ")
matrix2 = GetMatrix(rows, cols)
PrintMatrix(matrix2)
print("Matrix 1 + Matrix 2: ")
PrintMatrix(sumMatrix(matrix1, matrix2))
print()
print("Matrix 1 * Matrix 2: ")
PrintMatrix(mulMatrix(matrix1, matrix2))
