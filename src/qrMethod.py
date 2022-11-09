import numpy as np
import math

temp = [[1., 1., 0.],
       [1., 0., 1.],
       [0., 1., 1.]]

def identity(length):
    matrix = np.empty((1,length))
    for i in range(length):
        if(i == 0):
            matrix[0][i] = 1
        else:
            matrix[0][i] = 0
    return matrix.transpose()

def getCol(temp,col):
    matrix = np.empty((1,len(temp)))
    index = 0
    for i in range(len(temp)):
        matrix[0][index] = temp[i][col]
        index+= 1
    return matrix.transpose()

# tes extract 1 colomn dari sebuah matriks

def getLength(temp):
    sum = 0
    for elemnts in temp : 
        sum += elemnts ** 2
    return math.sqrt(sum)

def getV(matrixCol,i):

    length = getLength(matrixCol)
    # if(matrixCol[0][0] < 0 ):
    #     # u = matrixCol + length*identity(len(matrixCol))
    #     u = matrixCol + length*identity(len(matrixCol))
    # else:
    #     # u = matrixCol - length*identity(len(matrixCol))
    #     u = matrixCol - length*identity(len(matrixCol))
    if(matrixCol[0][0] > 0):
        length *= -1
    u = matrixCol - length*identity(len(matrixCol))
    v = u / getLength(u)
    
    return v

def getH(v):
    temp = np.dot(v,v.transpose())
    # temp2 = np.dot(v.transpose(),v)
    return(np.identity(len(v)) - 2 * temp)

def smallerMatrix(temp):
    matrix = np.empty((len(temp)-1,len(temp[0])-1))
    row = 0
    col = 0
    for i in range(1,len(temp)):
        for j in range(1,len(temp[0])):
            matrix[i-1][j-1] = temp[i][j]
            row +=1
            col += 1
    return matrix

def filledMatrix(matrix,length):
    identity = np.identity(length)
    row = 0 
    col = 0
    startingPointI = length - len(matrix)
    startingPointJ = length - len(matrix[0])
    for i in range(startingPointI,length):
        col = 0
        for j in range(startingPointJ,length):
            identity[i][j] = matrix[row][col]
            col += 1
        row += 1
    return identity

def qrMethods(matrixInput):

    H = np.empty((len(matrixInput[0])-1, len(matrixInput),len(matrixInput)))
    # H = np.arrange(H).reshape(len(matrixInput[0])-1,len(matrixInput))
    Q = np.empty((len(matrixInput),len(matrixInput[0])))
    R = np.empty((len(matrixInput),len(matrixInput[0])))
    temp = matrixInput
    for i in range(len(H)):
        
        # column = np.array(temp[:, i])
        column =  getCol(temp,0)
        v = getV(column,i)
        h = getH(v)
        if(i == 0):
            H[i] = h
        else:
            H[i] = filledMatrix(h,len(matrixInput))
        temp =np.dot(h,temp)
        temp = smallerMatrix(temp)
        # temp = np.delete(temp,0,0)
        
    for i in range(len(H)):
        if(i == 0):
            Q = H[0]
        else:
            Q = np.dot( Q, H[i])
    # print("============== Matriks Q ===========")
    # print(Q)

    for i in range(len(H)-1,-1,-1):
        if(i == len(H)-1):
            R = H[i]
        else:            
            R = np.dot(R,H[i])
    R = np.dot(R,matrixInput)
    # print("=========== Matriks R ==================")
    # print(R)
    # print("Matriks awal berdasarkan perkalian Q dan R : ")
    # print(np.dot(Q,R))
    # print(np.dot(Q,temp))
    return Q,R


w, v = np.linalg.eig(temp)
print(w)

# Q,R = qrMethods(temp)
# print(Q)
# print(R)

for i in range(100):
    Q,R = qrMethods(temp)
    temp = np.dot(R,Q)
print(Q)
print(R)
