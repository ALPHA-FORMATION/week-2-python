# Multiply two polynomials
# https://www.geeksforgeeks.org/problems/multiply-two-polynomals0721/1


def multiply_polynomials(a, b):

    result_size = len(a) + len(b) - 1
    result = [0] * result_size

    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] += a[i] * b[j]

    return result

A1 = [5, 0, 10, 6]
B1 = [1, 2, 4]
print("Output 1:", multiply_polynomials(A1, B1))  

A2 = [1, 9, 3, 4, 7]
B2 = [4, 0, 2, 5]
print("Output 2:", multiply_polynomials(A2, B2))  
