# Rotate matrix by 90 degree
# https://www.geeksforgeeks.org/problems/rotate-by-90-degree-1587115621/1


def rotate90Anticlockwise(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for j in range(n):
        for i in range(n // 2):
            mat[i][j], mat[n - 1 - i][j] = mat[n - 1 - i][j], mat[i][j]
    return mat  
def printMatrix(mat):
    for row in mat:
        print(row)
    print()
mat1 = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]
rotate90Anticlockwise(mat1)
print("Rotated mat1:")
printMatrix(mat1)
mat2 = [[1, 2],
        [3, 4]]
rotate90Anticlockwise(mat2)
print("Rotated mat2:")
printMatrix(mat2)
