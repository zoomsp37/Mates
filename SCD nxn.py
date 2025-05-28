import random
import numpy as np

print('Ingrese el tamaño de la matriz de coficientes: ')
n = int(input())

r=3

sol_vec = []
inc_vec = []

def sign(x):
    if x > 0:
        return '+'
    elif x < 0:
        return '-'
    else:
        return ''

if n == 2:
    for i in range(n):
        inc_vec=['x','y']
elif n == 3:
    for i in range(n):
        inc_vec=['x','y','z']
else:
    for i in range(n):
        inc_vec.append(f'x_{i+1}')


for i in range(n):
    sol_vec.append(random.randint(-r,r))

A = []

for i in range(n):
    A.append([])
    for j in range(n):
        A[i].append(random.randint(-r,r))

ceros = []
det = np.linalg.det(A)

for i in range(n):
    ceros.append(A[i].count(0))

for i in range(n):
    while ceros[i] > n-2 or det == 0:
        for j in range(n):
            A[i][j] = random.randint(-r,r)
        ceros[i] = A[i].count(0)

t_i = [0]*n

for i in range(n):
    for j in range(n):
        t_i[i] += A[i][j]*sol_vec[j]

r_1=''

for i in range(n):
    for j in range(n):
        if A[i][j] == 1 and j == 0:
            r_1 += inc_vec[j]
        elif A[i][j] == 1 and j != 0:
            r_1 = r_1 + '+' + inc_vec[j]
        elif A[i][j] == -1:
            r_1 = r_1 + '-' + inc_vec[j]
        elif A[i][j] == 0:
            continue
        elif A[i][j] > 0:
            r_1 = r_1 + '+ ' f'{A[i][j]}' + inc_vec[j]
        elif A[i][j] < 0:
            r_1 = r_1 + f'{A[i][j]}' + inc_vec[j]
    r_1 = r_1 + ' = ' + f'{t_i[i]}' +', '

print(f'La matriz de coeficientes es: {A} y su determinante es {int(det)} \n')
print(f'El vector solución es: {sol_vec} \n')
print(f'El vector de términos independientes es: {t_i} \n')

print('Matriz: \n \item \n \[ \n \left( \n \\begin{array}{','c'*n,'|c}')

for i in range(n):
    for j in range(n):
        if j < n-1:
            print(f'{A[i][j]} &', end=' ')
        else:
            print(f'{A[i][j]} & {t_i[i]}  \\\\')

print('\end{array} \n \\right). \n \] \n\n')


print('Llave: \n \[ \n \\text{(a)} \quad \n \left\{ \n \\begin{array}{rcrcrcr}')

for i in range(n):
    for j in range(n):
        
        if j == 0:
            if A[i][j] ==0:
                print(' &&', end=' ')
            elif A[i][j] == 1:
                print(f'{inc_vec[j]} &', end=' ')
            elif A[i][j] == -1:
                print(f'{sign(A[i][j])} & ',f'{inc_vec[j]} &', end=' ')
            elif A[i][j] > 0:
                print(f'& {abs(A[i][j])}',f'{inc_vec[j]} &', end=' ')
            else:
                print(f'{sign(A[i][j])} & ',f'{abs(A[i][j])}',f'{inc_vec[j]} &', end=' ')
        elif j < n-1 and j != 0:
            if A[i][j] ==0:
                print(' &&', end=' ')
            else:
                print(f'{sign(A[i][j])} & ',f'{abs(A[i][j])}',f'{inc_vec[j]} &', end=' ')
        else:
            if A[i][j] ==0:
                print(f' &&= {t_i[i]}  \\\\')
            else:
                print(f'{sign(A[i][j])} & ',f'{abs(A[i][j])}',f'{inc_vec[j]} & = {t_i[i]}  \\\\')
    

print('\end{array} \n \\right. \n \]\n\n')
