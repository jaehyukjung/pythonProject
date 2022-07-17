N, K = map(int, input().split())

lst = [x for x in range(2,N+1)]

cnt = 0
while (cnt != K):
    temp = []
    d = lst[0]
    for x in lst:
        if x == lst[0]:
            cnt += 1
        elif x % d ==0:
            cnt += 1
        else:
            temp.append(x)

        if cnt == K:
            print(x)
            break
    lst = temp.copy()

