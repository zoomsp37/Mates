import random

import numpy as np

print('Ingrese el tamaño de la matriz de coficientes: ')
n = int(input())

r = 3

A = [[1,2,3,1],[2,1,1,2],[3,3,2,3],[1,3,1,2]]

# for i in range(n):
#     A.append([])
#     for j in range(n):
#         A[i].append(random.randint(1,r))

det = np.linalg.det(A)

B = A

t=[[]]*n
t_temp = []

print(f'La matriz es {A}')
print(f'Su determinante es {det}')

for k in range(n-1):
    t_temp = t[k]
    for i in range(1,n):
        t_temp.append(B[i][k]/B[k][k])
        if B[k][k] == 0:
            continue
        else :
            for j in range(n):
                B[i][j] = B[i][j] - t[k][i-1]*B[0][j]

