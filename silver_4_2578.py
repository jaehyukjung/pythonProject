def check(lst:list):
    total_cnt = 0
    for i in range(5):
        cnt = 0
        for j in range(5):
            if lst[i][j] == 0:
                cnt += 1
        if cnt == 5:
            total_cnt += 1

    for i in range(5):
        cnt = 0
        for j in range(5):
            if lst[j][i] == 0:
                cnt += 1
        if cnt == 5:
            total_cnt += 1

    cnt = 0
    for i in range(5):
        if lst[i][i] == 0:
            cnt += 1
    if cnt == 5:
        total_cnt += 1

    cnt = 0
    for i in range(5):
        if lst[i][4-i] == 0:
            cnt += 1
    if cnt == 5:
        total_cnt += 1

    return total_cnt

lst = []
for _ in range(5):
    lst.append(list(map(int, input().split())))
lst2 =[]
for x in lst:
    lst2 += x


ans = []
for _ in range(5):
    ans = ans + list(map(int, input().split()))


i =0
for i in range(25):
    n = lst2.index(ans[i])
    lst[n//5][n%5] = 0
    if check(lst) >= 3:
        break

print(i+1)