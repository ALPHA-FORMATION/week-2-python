# Check if matrix is sparse
# https://www.geeksforgeeks.org/dsa/check-given-matrix-sparse-not/


def isSparseMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0]) if m > 0 else 0
    total_elements = m * n

    zero_count = 0
    for row in matrix:
        zero_count += row.count(0)

    return zero_count > total_elements // 2

if __name__ == "__main__":
    matrix1 = [
        [1, 0, 3],
        [0, 0, 4],
        [6, 0, 0]
    ]
    print("Yes" if isSparseMatrix(matrix1) else "No") 

    matrix2 = [
        [1, 2, 3],
        [0, 7, 8],
        [5, 0, 7]
    ]
    print("Yes" if isSparseMatrix(matrix2) else "No") 
