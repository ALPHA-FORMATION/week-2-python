# Transpose of matrix
# https://www.geeksforgeeks.org/problems/transpose-of-matrix-1587115621/1


def transposeMatrix(mat):
    n = len(mat)
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    return mat

if __name__ == "__main__":

    mat1 = [
        [1, 1, 1, 1],
        [2, 2, 2, 2],
        [3, 3, 3, 3],
        [4, 4, 4, 4]
    ]
    print("Transpose of matrix 1:")
    result1 = transposeMatrix(mat1)
    for row in result1:
        print(row)

    mat2 = [
        [1, 2],
        [9, -2]
    ]
    print("\nTranspose of matrix 2:")
    result2 = transposeMatrix(mat2)
    for row in result2:
        print(row)
