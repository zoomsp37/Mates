import random

print('Ingrese el tamaño de la matriz cuadrada: ')
n = int(input())

r=3

sol_vec = []
inc_vec = []

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

for i in range(n):
    ceros.append(A[i].count(0))

for i in range(n):
    while ceros[i] > 3:
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

print(f'La matriz de coeficientes es: {A} \n')
print(f'El vector solución es: {sol_vec} \n')
print(f'El vector de términos independientes es: {t_i} \n')
print(f'Los incógnitas son: {inc_vec} \n')

print(f'Cadena para \systeme: ' + r_1 + '\n')

print('Matriz: \n \item \n $ \n \left( \n \\begin{array}{','c'*n,'|c}')

for i in range(n):
    for j in range(n):
        if j < n-1:
            print(f'{A[i][j]} &', end=' ')
        else:
            print(f'{A[i][j]} & {t_i[i]}  \\\\')
    

print('\end{array} \n \\right) \n $\\\\')



    