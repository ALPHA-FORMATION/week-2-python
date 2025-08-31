# Add two polynomials
# https://www.geeksforgeeks.org/dsa/program-add-two-polynomials/


def addPolynomials(A, B):
    n = len(A)
    m = len(B)
    size = max(n, m)

    result = [0] * size

    for i in range(n):
        result[i] += A[i]

    for i in range(m):
        result[i] += B[i]

    return result

A = [5, 0, 10, 6]  
B = [1, 2, 4]      

sum_poly = addPolynomials(A, B)
print("Sum of polynomials:", sum_poly)
