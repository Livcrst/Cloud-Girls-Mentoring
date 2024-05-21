a,b,c = input().split(' ')

a = int(a)
b = int(b)
c = int(c)

def maior(x,y):
    maior = (x+y+abs(x-y))/2
    return int(maior)

ab = maior(a,b)
ac = maior(a,c)
bc = maior(b,c)

results = [ab,ac,bc]

print(f'{max(results)} eh o maior')