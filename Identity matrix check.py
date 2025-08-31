# Identity matrix check
# https://www.geeksforgeeks.org/dsa/program-print-identity-matrix/


def is_identity_matrix(mat):
    n = len(mat) 
    
    for i in range(n):
        for j in range(n):
            if i == j:
                if mat[i][j] != 1:
                    return False  
            else:
                if mat[i][j] != 0:
                    return False  
    return True


if __name__ == "__main__":

    mat1 = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

    mat2 = [
        [6, 10, 12, 0],
        [0, 5, 0, 0],
        [0, 0, 9, 0],
        [0, 0, 0, 1]
    ]

    print("Checking matrix 1:")
    for row in mat1:
        print(row)
    print("Is Identity Matrix?:", is_identity_matrix(mat1)) 

    print("\nChecking matrix 2:")
    for row in mat2:
        print(row)
    print("Is Identity Matrix?:", is_identity_matrix(mat2)) 
