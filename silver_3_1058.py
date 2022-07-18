testcase = int(input())

lst = []

for _ in range(testcase):
    lst.append(input())

visit = [[0 for _ in range(testcase)] for _ in range(testcase)]

for i in range(testcase):
    for j in range(testcase):
        for k in range(testcase):
            if j == k:
                continue

            elif lst[j][k] == 'Y' or (lst[j][i] == 'Y' and lst[i][k] == 'Y'):
                visit[j][k] = 1


ans = 0
for i in visit:
    ans = max(ans, sum(i))
print(ans)