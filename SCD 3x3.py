import random

r=3

x = random.randint(-r,r)
y = random.randint(-r,r)
z = random.randint(-r,r)

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

# r_1=''

# for i in range(3):
#     for j in range(3):
#         if A[i][j] == 1:
#             r_1 += f'x_{j+1}'
#         elif A[i][j] == -1:
#             r_1 += f'-x_{j+1}'
#         elif A[i][j] > 0:
#             r_1 += f'{A[i][j]}x_{j+1}'
#         elif A[i][j] < 0:
#             r_1 += f'{A[i][j]}x_{j+1}'
        
            

# print(f'r_1')