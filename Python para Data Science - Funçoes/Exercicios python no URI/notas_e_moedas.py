cedulas = float(input())

notas100=cedulas//100
notas50=cedulas%100//50
notas20=cedulas%100%50//20
notas10=cedulas%100%50%20//10
notas5=cedulas%10%50%20%10//5
notas2=cedulas%100%50%20%10%5//2

#Moedas
notas=cedulas%100%50%20%10%5%2//1
fifty_cents = cedulas%100%50%20%10%5%2%1//0.50
twenty_cents = cedulas%100%50%20%10%5%2%1%0.50//0.20
ten_cents = cedulas%100%50%20%10%5%2%1%0.50%0.20//0.10
five_cents = cedulas%100%50%20%10%5%2%1%0.50%0.20%0.10//0.05
one_cent = cedulas%100%50%20%10%5%2%1%0.50%0.20%0.10%0.05//0.01

print('NOTAS:')

print('{} nota(s) de R$ 100,00'.format(int(notas100)))
print('{} nota(s) de R$ 50,00'.format(int(notas50)))
print('{} nota(s) de R$ 20,00'.format(int(notas20)))
print('{} nota(s) de R$ 10,00'.format(int(notas10)))
print('{} nota(s) de R$ 5,00'.format(int(notas5)))
print('{} nota(s) de R$ 2,00'.format(int(notas2)))


print('MOEDAS:')
print('{} moeda(s) de R$ 1,00'.format(int(notas)))
print('{} moeda(s) de R$ 0.50'.format(int(fifty_cents)))
print('{} moeda(s) de R$ 0.20'.format(int(twenty_cents)))
print('{} moeda(s) de R$ 0.10'.format(int(ten_cents)))
print('{} moeda(s) de R$ 0.05'.format(int(five_cents)))
print('{} moeda(s) de R$ 0.01'.format(int(one_cent)))

