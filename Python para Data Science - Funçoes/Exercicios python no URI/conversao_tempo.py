entry = int(input())

hour = entry//3600
minute = entry%3600//60
seconds = entry%3600%60

print(f'{hour}:{minute}:{seconds}')