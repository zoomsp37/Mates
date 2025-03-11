import random

r=3

x = random.randint(-r,r)
y = random.randint(-r,r)
z = random.randint(-r,r)

A = [[random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)], 
     [random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)], 
     [random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)]]

print(A)

t_i=[0,0,0]

for i in range(3):
    for j in range(3):
        t_i[i] += A[i][j]*[x,y,z][j]

print(t_i)

