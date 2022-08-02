N = int(input())

lst = [int(input()) for _ in range(N)]

lst.sort()
lst.reverse()
i = 0
m = -1
while i < len(lst)-2:
    if lst[i] < lst[i+1]+lst[i+2]:
        m = lst[i]+lst[i+1]+lst[i+2]
        break
    else:
        i += 1

print(m)