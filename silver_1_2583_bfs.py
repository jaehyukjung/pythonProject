from collections import deque
import sys
input = sys.stdin.readline

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

deq = deque()
result = []
for i in range(M):
    for j in range(N):
        if maps[i][j] == 0:
            maps[i][j] = 1
            deq.append((i,j))
            count = 1
            while(len(deq) != 0):
                x, y = deq.popleft()
                for k in range(4):
                    nx = x+dx[k]
                    ny = y+dy[k]
                    if 0<=nx< M and 0<=ny<N and maps[nx][ny] ==0:
                        deq.append((nx,ny))
                        maps[nx][ny] = 1
                        count += 1
            result.append(count)

print(len(result))
print(*sorted(result))
