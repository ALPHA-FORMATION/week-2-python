# Sum of diagonals
# https://www.geeksforgeeks.org/problems/sum-of-diagonals-1587115621/1


def sumDiagonal(N, M):
    sum_ = 0
    for i in range(N):
        sum_ += M[i][i]
    return sum_

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        elements = list(map(int, input().split()))

        M = []
        index = 0
        for i in range(N):
            row = elements[index : index + N]
            M.append(row)
            index += N

        print(sumDiagonal(N, M))

if __name__ == "__main__":
    main()
