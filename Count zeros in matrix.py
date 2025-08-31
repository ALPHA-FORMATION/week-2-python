# Count zeros in matrix
# https://www.geeksforgeeks.org/problems/count-zeros-in-a-sorted-matrix/1


def countZeros(A):
    n = len(A)
    row = 0
    col = n - 1
    count = 0

    while row < n and col >= 0:
        if A[row][col] == 0:
            count += (col + 1)
            row += 1
        else:
            col -= 1

    return count

if __name__ == "__main__":
    N = int(input("Enter N (size of matrix): "))

    print("Enter the matrix row by row (space-separated 0s and 1s):")
    A = []
    for _ in range(N):
        row = list(map(int, input().strip().split()))
        A.append(row)

    result = countZeros(A)
    print("Total number of zeros:", result)
