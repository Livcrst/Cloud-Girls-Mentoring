old = int(input())

year = old//365
month = (old%365)//30
day = (old%365)%30

print(f'{year} ano(s)\n{month} mes(es)\n{day} dia(s)')