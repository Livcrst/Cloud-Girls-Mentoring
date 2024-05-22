from math import sqrt

a,b,c = map(float, input().split(' ')) #recebe meus dados

delta = b**2 - 4*a*c #calculo do delta
if delta> 0 and 2*a > 0:
    R1 = ( -b + sqrt(delta)) / 2*a #calculo da primeira raiz
    R2 = ( -b - sqrt(delta)) / 2*a #calculo da primeira raiz
    print('R1 = {:.5f}'.format(R1)) #imprime a primeira raiz
    print('R2 = {:.5f}'.format(R2)) #imprime a segunda raizcls
else: 
    print('Impossivel calcular')