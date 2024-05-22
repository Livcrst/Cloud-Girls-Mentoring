x,y = map(float, input().split(' '))

if not (x == 0 and y == 0):
    # Coordenadas positivas são quadarante 1
    if x > 0 and y > 0:
        print('Q1')
    # y positivo e x negativo quadrante 2
    elif x < 0 and y > 0:
        print('Q2')
    #  ambas coordenadas negativas quaadrante 3 
    elif x < 0 and y < 0:
        print('Q3')
    # x positivo e y negativo quadante 4
    elif x > 0 and y < 0:
        print('Q4')
elif x > 0 and y == 0:
    print('Eixo X')
elif x==0 and y > 0:
    print('Eixo Y')
else:
    print('Origem')