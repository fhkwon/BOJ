h, m = map(int, input().split())
cm = int(input())

h += cm // 60
m += cm % 60

while m > 59:
    m -= 60
    h += 1

while h > 23:
    h -= 24
    
print(f'{h} {m}')