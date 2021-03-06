import numpy as np
import copy

matrix1 = [[3, -7, -2, 2], [-3, 5, 1, 0], [6, -4, 0, -5], [-9, 5, -5, 12]]
matrix2 = [[0.5, 1, 1.5, 2], [1, 2.5, 4, 3.5], [1.5, 4, 7.5, 7], [2, 3.5, 7, 13.5]]
matrix3 = [[3, 1, -1], [1, 1, -2], [-6, -3, 2]]
matrix4 = [[1,2],[3,8]]
n1 = [[1, 2, 3], [12, 4, 5], [1, 2, 4]]
n = [[1, 2, 3], [1, 2, 4], [12, 4, 5]]
m = [[0,1,2],[0,0,1],[1,1,0]]
mm = [[1,1,1],[1,1,1],[1,1,1]]
matr = [[1,2,3],[4,5,6],[7,8,9]]


identity_matrix = lambda dim: [[1 if j == i else 0 for j in range(dim)] for i in range(dim)]


def is_nonsingular(matrix):
    dim = len(matrix)
    if dim != len(matrix[0]):
        raise Exception("Matrix is not square")
    matrixcopy = copy.deepcopy(matrix)
    if(dim == 2):
        return (matrixcopy[0][0] * matrixcopy[1][1] - matrixcopy[1][0] * matrixcopy[0][1] != 0)
    for i in range(dim):
        for j in range(dim - 1):
            matrixcopy[i].append(matrixcopy[i][j])
    det = 0.0
    for j in range(dim):
        mult_to_add = 1
        mult_to_substr = 1
        for i in range(dim):
            mult_to_add = (float)(mult_to_add * matrixcopy[i][i + j])
            mult_to_substr = (float)(mult_to_substr * matrixcopy[(dim - 1 - i)][i + j])
        det = (float)(det + (mult_to_add - mult_to_substr))
    if det != 0:
        return True
    else:
        return False


def LU_factorization(matrix):
    dim = len(matrix)
    matrixc = copy.deepcopy(matrix)
    L = [[0] * dim for i in range(dim)]
    U = identity_matrix(dim)
    P = identity_matrix(dim)
    for k in range(1, dim + 1):
        if matrixc[k - 1][k - 1] == 0:

            Ptemp = permutation(matrixc,k-1)
            L = np.dot(Ptemp,L)
            matrixc = np.dot(Ptemp,matrixc)
            P = np.dot(Ptemp,P)

        for i in range(k - 1, dim):
            summ = 0
            for p in range(k - 1):
                summ += L[i][p] * U[p][k - 1]
            L[i][k - 1] = matrixc[i][k - 1] - summ
        if L[k - 1][k - 1] == 0:

            Ptemp = permutation(L, k - 1)
            L = np.dot(Ptemp, L)
            matrixc = np.dot(Ptemp,matrixc)
            P = np.dot(Ptemp, P)

        for j in range(k, dim):
            summ = 0
            for p in range(k - 1):
                summ += L[k - 1][p] * U[p][j]
            U[k - 1][j] = (float)(matrixc[k - 1][j] - summ) / L[k - 1][k - 1]
    return L, U, P

def permutation(matrix,k):
    dim = len(matrix)
    i = k + 1
    b = False
    P = identity_matrix(dim)
    while b is False and i != dim:
        if matrix[i][k] != 0:
            swap = P[k]
            P[k] = P[i]
            P[i] = swap
            b = True
        else:
            i += 1
    if b is False:
        raise Exception("Matrix can't be permuted properly")
    return P



def inversion(matrix):
    dim = len(matrix)
    Iinv = identity_matrix(dim)
    for j in range(dim):
        E = identity_matrix(dim)
        pivot = (float)(matrix[j][j])
        for i in range(dim):
            E[i][j] = (float)(-matrix[i][j]) / (pivot)
        E[j][j] = 1.0/ pivot
        matrix = np.dot(E, matrix)
        Iinv = np.dot(E, Iinv)
    return Iinv


def inv_with_LU(matrix):
#    if not is_nonsingular(matrix):                    #this function still works properly without using
#       raise Exception("This matrix is singular")    #is_nonsingular() func. In this case uncomment 2 next lines
    if len(matrix) != len(matrix[0]):
       raise Exception("Matrix is not square")
    L, U, P = LU_factorization(matrix)
    Linv = inversion(L)
    Uinv = inversion(U)
    matrix =  np.dot(Uinv, Linv)
    return np.dot(matrix,P)


def print_matrix(matrix):
    for i in matrix:
        print i


#L, U, P = LU_factorization(matr)
print("________________________")
#print_matrix(matr)
print("________________________")
#print_matrix(L)
print("________________________")
#print_matrix(U)
print("________________________")
#print_matrix(np.dot(L, U))
print("________________________")
#print_matrix(inv_with_LU(n))
print("________________________")
#print_matrix(inversion(n1))
print("________________________")
#print_matrix(inv_with_LU(n1))
print("________________________")
#print_matrix(inv_with_LU(m))
print("________________________")
print_matrix(inv_with_LU(matrix2))
print("________________________")
print_matrix(inversion(matrix2))
