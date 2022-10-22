M, N, K = map(int, input().split())

maps = [[0 for _ in range(N)] for _ in range(M)]

for i in range(K):
    x1,y1,x2,y2 = map(int, input().split())
    for j in range(y1,y2):
        for k in range(x1,x2):
            maps[j][k] = 1
count = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x, y):
    global count
    if x < 0 or x >= M or y < 0 or y >= N:
        return 0
    if maps[x][y] == 1:
        return 0

    maps[x][y] = 1
    count += 1
    for i in range(4):
        dfs(x + dx[i], y + dy[i])

    return count

result = []
for i in range(M):
    for j in range(N):
        if maps[i][j] == 0:
            result.append(dfs(i,j))
            count = 0

result.sort()
print(len(result))
for i in result:
    print(i, end= " ")



