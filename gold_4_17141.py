import sys
from collections import deque
from itertools import combinations

def bfs(virus_list):
    q = deque()
    v = [[-1]*n for _ in range(n)]

    for i,j in virus_list:
        q.append((i,j))
        v[i][j] = 0

    while q:
        ci,cj = q.popleft()

        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci + di,cj + dj
            if 0<=ni<n and 0<=nj<n:
                if v[ni][nj] == -1 and arr[ni][nj] != 1:
                    q.append((ni,nj))
                    v[ni][nj] = v[ci][cj] + 1
    for i in range(n):
        if v[i].count(-1) != arr[i].count(1):
            return n**2

    return max(map(max,v))


if __name__ == "__main__":
    n,m = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    virus = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                virus.append((i,j))
    ans = n**2
    for virus_list in combinations(virus,m):
        ans = min(ans, bfs(virus_list))

    if ans == n**2:
        print(-1)
    else:
        print(ans)