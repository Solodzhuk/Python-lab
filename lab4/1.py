from sympy import symbols, Matrix

lambda_param, rho_param, mu_param = symbols('lambda rho mu')
matrix = Matrix([[0, 0, 0, -1/rho_param, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, -1/rho_param, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, -1/rho_param, 0, 0, 0],
                  [-1*(lambda_param + 2*mu_param), 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, -1*mu_param, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, -1*mu_param, 0, 0, 0, 0, 0, 0],
                  [-1*lambda_param, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [-1*lambda_param, 0, 0, 0, 0, 0, 0, 0, 0]])

print(matrix)

eigenvects = matrix.eigenvects()
print("")
for val in eigenvects:
    value = val[0]
    quantity = val[1]
    vectors = val[2]
    print("собственное значение", value)
    print("Количество собственных векторов для данного значения:", quantity)
    for vector in vectors:
        print(vector, "\n")