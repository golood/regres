import numpy as np
from scipy.optimize import linprog
x = np.array([[2, 5],
          [9, 4],
          [6, 1],
          [8, 3],
          [1, 7],
          [5, 8]])

A = np.array([2, 5, -2, -5, ])

y = [7, 9, 1, 6, 4, 5]

b_ub = [74,40,36]
b_eq = [20,45,30]
A=np.array([[7, 3,6],[4,8,2],[1,5,9]])
m, n = A.shape
c=list(np.reshape(A,n*m))# Преобразование матрицы A в список c.
m1, n1 = x.shape
c1=list(np.reshape(x,n1*m1))# Преобразование матрицы A в список c.

print(c1)

A_eq= np.zeros([m1,m1*n1])
for i in np.arange(0,m1,1):# Заполнение матрицы условий –равенств.
    k=0
    for j in np.arange(0,n1*m1,1):
        if j==k*n1+i:
            A_eq [i,j]=1
            k=k+1
# print(linprog(c, A_ub, b_ub, A_eq, b_eq))
# print(linprog(c1, A_eq=A_eq, b_eq=y, method='revised simplex'))
