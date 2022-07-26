h, w = map(int, input().split())

lst = list(map(int, input().split()))

ans = 0
for i in range(1,w-1):
    lmax = max(lst[:i])
    rmax = max(lst[i+1:])

    if lmax > lst[i] and rmax > lst[i]:
        ans += min(lmax, rmax) - lst[i]

print(ans)

