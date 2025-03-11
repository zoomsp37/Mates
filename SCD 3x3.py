import random

r=3

x = random.randint(-r,r)
y = random.randint(-r,r)
z = random.randint(-r,r)

sol_vec = [x,y,z]
inc_vec =['x','y','z']

A=[[0,0,0],[0,0,0],[0,0,0]]

ceros0 = A[0].count(0)
ceros1 = A[1].count(0)
ceros2 = A[2].count(0)
no_tries = 0


while ceros0>1 or ceros1>1 or ceros2>1:
    A = [[random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)], 
        [random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)], 
        [random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)]]
    ceros0 = A[0].count(0)
    ceros1 = A[1].count(0)
    ceros2 = A[2].count(0)
    no_tries += 1

t_i=[0,0,0]

for i in range(3):
    for j in range(3):
        t_i[i] += A[i][j]*[x,y,z][j]



print(f'La matriz de coeficientes es: {A}, después de {no_tries} intentos \n')
print(f'El vector solución es: [{x},{y},{z}] \n')
print(f'El vector de términos independientes es: {t_i} \n')

r_1=''

for i in range(3):
    for j in range(3):
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

print(f'Cadena para \systeme: ' + r_1 + '\n')

print('Matriz: \n \item \n $ \n \left( \n \\begin{array}{ccc|c}')
print(f'{A[0][0]} & {A[0][1]} & {A[0][2]} & {t_i[0]} \\\\')
print(f'{A[1][0]} & {A[1][1]} & {A[1][2]} & {t_i[1]} \\\\')
print(f'{A[2][0]} & {A[2][1]} & {A[2][2]} & {t_i[2]} \\\\')
print('\end{array} \n \\right) \n $\\\\')

