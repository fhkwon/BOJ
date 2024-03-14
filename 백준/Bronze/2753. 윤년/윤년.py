Y = int(input())

ans = 0
if Y%4 == 0:
    if Y%100 != 0:
        ans = 1
    elif Y%400 == 0:
        ans = 1

print(ans)