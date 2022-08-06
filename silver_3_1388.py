n, m = map(int, input().split())

lst = [[x for x in input()] for _ in range(n)]

cnt1 = 0
for i in range(n):
    j = 0
    while(j < m):
        if lst[i][j] == '-':
            cnt1 += 1
            while j < m-1:
                if lst[i][j+1] == '-':
                    j += 1
                else:
                    break
        j +=1
cnt2 =0
for i in range(m):
    j = 0
    while (j < n):
        if lst[j][i] == '|':
            cnt2 += 1
            while j < n-1:
                if lst[j+1][i] == '|':
                    j += 1
                else:
                    break
        j += 1
print(cnt1+cnt2)