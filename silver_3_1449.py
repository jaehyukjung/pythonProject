n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

cnt = 0
i = 0
k = 1
while i < n:
    while i + k < n:
        if lst[i+k] <= lst[i] + m - 1:
            k += 1
        else:
            break
    cnt += 1
    i += k
    k = 1

print(cnt)