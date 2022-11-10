from sympy import Matrix
from qrMethod import *  
import numpy as np
# List A 
A = [[2.92,0.86,-1.15],[0.86,6.51,3.32],[-1.15,3.32,4.57]]
# Matrix A


def copyMatrix(A):
    temp = A
    return temp
temp = copyMatrix(A)
for i in range(50):
    print("====== Hasil pake fungsi bawaan ========")
    Q, R = getQr(temp)
    print(Q)
    if(i == 0):
        eigenVector = Q
    else:
        eigenVector = np.dot(eigenVector,Q)
    temp = np.dot(R,Q)
print(eigenVector)
Q1,R1 = np.linalg.qr(A)
print("======== Hasil pake fungsi python ====")
print(Q1)

v,w = np.linalg.eig(A)
print(w)
