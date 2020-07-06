import cmath
import numpy as np

# matrix dimensions and row/col split
# is same as 2D-list
A = np.array([[1, 1], [2, 1]])
print("\nA =\n", A, sep="")
print("\nInverse of A:\n", np.linalg.inv(A))  # inversion of matrix

B = np.array([[2, 4], [1, 5]])
print("\nB =\n", B, sep="")

# np.matmul for matrix multiplication
print("\nMatrix mult. of A and B:\n", np.matmul(A, B), sep="")


def eqsys_ex():
    # Asssuming A is coefficient matrix
    A = np.array([[1, 1, 1], [2, 1, 1], [4, 3, -1]])
    B = np.array([[2], [3], [4]])

    # The solution is inv(A) multiplied (left side) with B
    X = np.matmul(np.linalg.inv(A), B)
    print("The solution is:\n", X)

