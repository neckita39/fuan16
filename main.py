import math

from array import *
import numpy as np
from numpy import linalg as LA
from math import sqrt

print("-+-+-+-+-+-+-+-+-+-+-")
A = np.array([[6, -1, 10, -1],
              [2, 1, 10, 7],
              [3, -2, -2, -1],
              [1, -12, 2, -1]])
b = np.array([[158], [128], [7], [17]])
print("A^T*A")
atrans = A.transpose()
ATonA = atrans.dot(A)
print(ATonA)
print("-+-+-+-+-+-+-+-+-+-+-")
E = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])
wa, va = LA.eigh(ATonA)
print(wa)
alphomax = max(wa)
print("alpha(A^T*A)")
print(alphomax)
print("-+-+-+-+-+-+-+-+-+-+-")
c = (E - (ATonA / alphomax))
print("C matrix")
print(c)
print("-+-+-+-+-+-+-+-+-+-+-")
d = atrans.dot(b / alphomax)
print("d matrix")
print(d)
print("-+-+-+-+-+-+-+-+-+-+-")
wc, vc = LA.eigh(c)
print(wc)
print("alpha(C)")
k = max(wc)
print(k)
print("-+-+-+-+-+-+-+-+-+-+-")
x0 = np.array([[0], [0], [0], [0]])
x1 = c.dot(x0) + d
print("x1")
print(x1)
print("-+-+-+-+-+-+-+-+-+-+-")
ro = sqrt(pow(x1[0] - x0[0], 2) + pow(x1[1] - x0[1], 2) + pow(x1[2] - x0[2], 2) + pow(x1[3] - x0[3], 2))
print("ro(x0,x1)")
print(ro)
print("-+-+-+-+-+-+-+-+-+-+-")
print("Napri1")
print(math.log(pow(10, -2) * (1 - k) / ro, k))
print("-+-+-+-+-+-+-+-+-+-+-")
print("Napri2")
print(math.log(pow(10, -4) * (1 - k) / ro, k))
print("-+-+-+-+-+-+-+-+-+-+-")
print("e=10^-2")
copy_x0 = x0
copy_x1 = x1
ro2 = sqrt((x0[0] - x1[0]) ** 2 + (x0[1] - x1[1]) ** 2 + (x0[2] - x1[2]) ** 2 + (x0[3] - x1[3]) ** 2)
i = 0
while (k / (1 - k)) * ro2 > 10 ** (-2):
    x0 = x1
    x1 = c.dot(x0) + d
    ro2 = sqrt((x0[0] - x1[0]) ** 2 + (x0[1] - x1[1]) ** 2 + (x0[2] - x1[2]) ** 2 + (x0[3] - x1[3]) ** 2)
    i += 1
xe2 = x1
print(xe2)
print(i)
print("-+-+-+-+-+-+-+-+-+-+-")
print("e=10^-4")
x0 = copy_x0
x1 = copy_x1
ro2 = sqrt((x0[0] - x1[0]) ** 2 + (x0[1] - x1[1]) ** 2 + (x0[2] - x1[2]) ** 2 + (x0[3] - x1[3]) ** 2)
i = 0
while (k / (1 - k)) * ro2 > 10 ** (-4):
    x0 = x1
    x1 = c.dot(x0) + d
    ro2 = sqrt((x0[0] - x1[0]) ** 2 + (x0[1] - x1[1]) ** 2 + (x0[2] - x1[2]) ** 2 + (x0[3] - x1[3]) ** 2)
    i += 1
xe4 = x1
print(xe4)
print(i)
print("-+-+-+-+-+-+-+-+-+-+-")
x = np.array([[10],
              [6],
              [20],
              [35]])
roXe2X = sqrt((x[0] - xe2[0]) ** 2 + (x[1] - xe2[1]) ** 2 + (x[2] - xe2[2]) ** 2 + (x[3] - xe2[3]) ** 2)
print(roXe2X)
print("-+-+-+-+-+-+-+-+-+-+-")
x = np.array([[10],
              [6],
              [20],
              [35]])
roXe2X = sqrt((x[0] - xe4[0]) ** 2 + (x[1] - xe4[1]) ** 2 + (x[2] - xe4[2]) ** 2 + (x[3] - xe4[3]) ** 2)
print(roXe2X)
print("-+-+-+-+-+-+-+-+-+-+-")



