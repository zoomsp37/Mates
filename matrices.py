import random

r=3

def mat_prod(A,B):
    C = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k]*B[k][j]
    return C

x = random.randint(-r,r)

A = [[random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)], 
     [random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)], 
     [random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)]]

B = [[random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)], 
     [random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)], 
     [random.randint(-r,r), random.randint(-r,r), random.randint(-r,r)]]

print(A)
print(B)

print(mat_prod(A,B))
