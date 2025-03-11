import random



count = 0

for a in range(-10, 10):
    for b in range(-10, 10):
        for c in range(-10, 10):

            disc = (-a*b-a*c)*(-a*b-a*c)-(4*a*a*b*c)
            if disc > 0 and a%3 == 0 and c != 0 and abs(a*b*c) < 60 and (-a*b-a*c) % 2 == 0 and abs((-a*b-a*c)/2) < 20 and a/3 == 1:
                if a/3 == 1:
                    print(f'\item $x^3 + {int((-a*b-a*c)/2)}x^2 + {int(a*b*c)}x$' + chr(92) + chr(92))
                
                print(f'\item ${int(a/3)}x^3 + {int((-a*b-a*c)/2)}x^2 + {int(a*b*c)}x$' + chr(92) + chr(92))
                count += 1

print(f'{count} polinomios de tercer grado con extremos relativos en valores enteros de x') 
