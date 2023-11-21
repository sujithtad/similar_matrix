def matrix_multiply(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            product = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))
            row.append(product)
        result.append(row)
    return result
