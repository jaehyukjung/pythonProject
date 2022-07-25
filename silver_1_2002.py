N = int(input())

en = [input() for _ in range(N)]
ex = [input() for _ in range(N)]

ans = 0

for i in range(N-1):
    cnt = 0
    for j in range(N):
        if ex[i] == en[j]:
            for x in en[:j]:
                if x in ex[i+1:]:
                    cnt += 1

    if cnt >= 1:
        ans += 1

print(ans)
