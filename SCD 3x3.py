import random

r=3

x = random.randint(-r,r)
y = random.randint(-r,r)
z = random.randint(-r,r)

sol_vec = [x,y,z]
inc_vec =['x','y','z']

A = [[random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)], 
     [random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)], 
     [random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)]]

t_i=[0,0,0]

for i in range(3):
    for j in range(3):
        t_i[i] += A[i][j]*[x,y,z][j]

print(f'La matriz de coeficientes es: {A}')
print(f'El vector solución es: [{x},{y},{z}]')
print(f'El vector de términos independientes es: {t_i}')

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

print(f'La respuesta es:' + r_1)