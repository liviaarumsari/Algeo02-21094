import numpy as np
from sympy import *

temp = [
    [2, 3, 4, 5, 6],
    [4, 4, 5, 6, 7],
    [0, 3, 6, 7, 8],
    [0, 0, 2, 8, 9],
    [0, 0, 0, 1, 10],
]


def checkTriangle(matrix):
    for i in range(1, len(matrix)):
        for j in range(0, i):
            if matrix[i][j] != 0:
                return False
    return True


def getLength(matrix):
    result = 0
    for i in matrix:
        result += i**2
    result = result ** (1 / 2)
    return result


def identityCol(length):
    matrix = [[0 for i in range(length)] for j in range(1)]
    matrix = np.array(matrix)
    matrix[0][0] = 1
    return matrix.transpose()


def getU(matrixCol):
    matrixCol = np.reshape(matrixCol, (len(matrixCol), 1))
    # Menghitung proyeksi dari matrix 1  ke matrix 2
    if matrixCol[0] < 0:
        u = matrixCol - getLength(matrixCol) * identityCol(len(matrixCol))
    else:
        u = matrixCol + getLength(matrixCol) * identityCol(len(matrixCol))
    return u


def getH(matrix):
    pembilang = np.dot(matrix, matrix.transpose())
    penyebut = np.dot(matrix.transpose(), matrix)
    h = np.identity(len(matrix)) - 2 * pembilang / penyebut
    return h


def filledMatrix(matrix, length):
    identity = np.identity(length)
    row = 0
    col = 0
    startingPointI = length - len(matrix)
    startingPointJ = length - len(matrix[0])
    for i in range(startingPointI, length):
        col = 0
        for j in range(startingPointJ, length):
            identity[i][j] = matrix[row][col]
            col += 1
        row += 1
    return identity


def copyMatrix(matrix):
    copy = np.array(matrix)
    return copy


def getQr(matrix):
    matrix = np.array(matrix)
    # H = np.empty(len(matrix))
    matrixTemp = np.array(matrix)
    for i in range(len(matrixTemp[0])):
        if checkTriangle(matrixTemp) == False:
            temp = matrixTemp[:, 0]
            temp = np.reshape(temp, (len(temp), 1))
            u = getU(temp)
            h = getH(u)
            if i == 0:
                Q = h
                R = np.dot(h, matrixTemp)
            else:
                htemp = filledMatrix(h, len(matrix))
                Q = np.dot(Q, htemp)
                R = np.dot(htemp, R)
            matrixTemp = np.dot(h, matrixTemp)
            matrixTemp = np.delete(matrixTemp, 0, 0)
            matrixTemp = np.delete(matrixTemp, 0, 1)
    return Q, R


def searchEigenVector(eigenValues, matrix):
    n = len(matrix)
    identity = np.identity(n)
    for i in range(len(eigenValues)):
        print(identity)
        tempMatrix = eigenValues[i] * identity - matrix
        tempMatrix = Matrix(tempMatrix)
        basisVektor = tempMatrix.nullspace()
        if not basisVektor:
            basisVektor = np.zeros((len(matrix), 1))
        if i == 0:
            arr = basisVektor
        else:
            arr = np.append(arr, basisVektor, axis=1)


matrix = copyMatrix(temp)

for i in range(500):
    q, r = getQr(matrix)
    matrix = np.dot(r, q)
    if i == 0:
        basisVector = q
    else:
        basisVector = np.dot(basisVector, q)
eigenValues = matrix.diagonal()
