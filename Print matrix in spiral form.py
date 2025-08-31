# Print matrix in spiral form
# https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1


def spiralOrder(mat):
    if not mat or not mat[0]:
        return []
    n = len(mat)      
    m = len(mat[0])   
    result = []
    top = 0
    bottom = n - 1
    left = 0
    right = m - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1
    return result
mat1 = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]]
mat2 = [[2, 7, 10],
        [5, 1, 3],
        [4, 2, 8]]
mat3 = [[32, 44, 27, 23],
        [54, 28, 50, 62]]
print("Output for mat1:")
print(spiralOrder(mat1))  
print("\nOutput for mat2:")
print(spiralOrder(mat2))  
print("\nOutput for mat3:")
print(spiralOrder(mat3))  
