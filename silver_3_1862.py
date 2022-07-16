N = int(input())

ans = 0
for i in range(len(str(N))):
    one = N % 10
    N = N // 10

    if one >= 5:
        ans += (one-1) * (9 ** i)
    else:
        ans += one * (9 ** i)

print(ans)