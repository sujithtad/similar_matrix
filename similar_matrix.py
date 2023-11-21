from matix_operations.inverse import getMatrixInverse
from matix_operations.multiply import matrix_multiply


def get_matrix_b(mat_a, mat_p):
    return matrix_multiply(matrix_multiply(getMatrixInverse(mat_p), mat_a), mat_p)


def get_matrix_a(mat_b, mat_p):
    return matrix_multiply(matrix_multiply(mat_p, mat_b), (getMatrixInverse(mat_p)))


def get_user_input():
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))

    # Initialize matrix
    matrix = []
    print("Enter the entries rowwise:")

    # For user input
    for i in range(R):  # A for loop for row entries
        a = []
        for j in range(C):  # A for loop for column entries
            a.append(int(input()))
        matrix.append(a)
    return matrix


def main():
    print("For A:")
    mat_a = get_user_input()
    print("For P:")
    mat_p = get_user_input()
    print("Matrix B")
    print(get_matrix_b(mat_a, mat_p))


if __name__ == "__main__":
    main()
